import numpy as np
from scipy.signal import savgol_filter,find_peaks
try:
    import afmformats
except:
    print('You have an old version of afmformats installed.')

from .curve import (MODE_DIRECTION_BACKWARD, MODE_DIRECTION_FORWARD,
                    MODE_DIRECTIONS_PAUSE, Segment)
from .mvFilesystem import MvNode

class DataSet(MvNode):
    _leaf_ext = ['.txt']

    def __init__(self, filename=None, parent=None):
        super().__init__(parent=parent, filename=filename)
        self._header = None
        self.cantilever_k = 1.0  # elastic constant of the cantilever in nN/nm
        self.cantilever_lever = 1.0  # calibration factor InvOls in nm/V
        self.cantilever_type = 'Colloidal probe'
        # the name of the file the text output was created from
        self.original_filename = None
        self.tip_radius = 1000.0  # radius of the tip, used for sphere, in nm, or angle in deg
        self.tip_shape = None  # onest shapes are 'sphere' , 'cone' , 'cylinder', 'pyramid'
        # store for the full time tracks, add additional channels
        self.data = {'time': [], 'force': [], 'deflection': [], 'z': []}
        self.protocol = []  # a list of protsegments parameters
        # in case a default speed was set and it is not readable from the segment
        self.protocol_speed = None
        self.version = None
        self.forwardSegment = 0
        self.hertz = {}
        self.hertz['threshold'] = None
        self.hertz['thresholdType'] = 'indentation'
        self.xpos = None
        self.ypos = None
        self.valid = True
        self.curveid = 0

    def setRadius(self, value, recursive=True):
        self.tip_radius = value
        if recursive is True:
            for c in self.haystack:
                c.tip_radius = value

    def setForwardSegment(self, value, recursive=True):
        self.forwardSegment = value
        if recursive is True:
            for c in self.haystack:
                c.forwardSegment = value

    def open(self):
        self.header()
        self.load()
        self.createSegments()

    def check(self):
        # Implement this function to get a signature of the filetype (not only by the extension)
        return True  # True = this is a known file, False otherwise

    def header(self):
        # Implement this function to populate the header, see the constructor for critical info
        pass

    def load(self):
        pass

    def createSegments(self):
        pass


##################################
##### Optics11 Chiaro ############
##################################

def cross(x1, x2, th, dth):
    th1 = th+dth
    th2 = th-dth
    if np.sign(x1-th1) != np.sign(x2-th1):
        return True
    if np.sign(x1-th2) != np.sign(x2-th2):
        return True
    return False

def toFloat(val):
    return float(val.replace(',', '.'))

class ChiaroBase(DataSet):

    def check(self):
        f = open(self.filename,encoding='latin1')
        signature = f.readline()
        f.close()
        if signature[0:5] == 'Date\t':
            return True
        return False

    def getTarget(self,line,target):
        init = len(target)
        if line[init]==':':
            init+=1
        value = line[init:].strip()
        return value

    def header(self):
        self.tip_shape = 'sphere'
        f = open(self.filename,encoding='latin1')

        self.O11={'device':'Chiaro','version':'old','SMDuration':0}

        targets = ['Tip radius (um)', 'Calibration factor', 'k (N/m)', 'SMDuration (s)',
                   'Profile:', 'E[eff] (Pa)', 'X-position (um)', 'Y-position (um)',
                   'Software version','Time (s)','Measurement','Loading / unloading time (s)','Depth (nm)',
                   'Z-position (um)','Z surface (um)','Piezo position (nm) (Measured)', 'Calibration factor',
                   'Device', 'Software version','Control mode','Measurement','SMDuration']

        startprotocol = ['Profile','Piezo Indentation Sweep Settings']

        #Reading header    
        self.version = 'old'

        for line in f:
            starting = False
            for start in startprotocol:
                if start in line:
                    starting = True
                    break
            if starting is True:
                break
            targeted = False
            for target in targets:
                if target in line:
                    targeted = True
                    break
            if targeted is True:
                value = self.getTarget(line,target)
                if target=='Tip radius (um)':
                    self.tip_radius = toFloat(value)*1000.0  # NB: internal units are nm
                elif target == 'k (N/m)':
                    self.cantilever_k = toFloat(value)
                elif target =='Calibration factor':
                    self.cantilever_lever = toFloat(value)  # NB: so called geometric factor
                elif target=='E[eff] (Pa)':
                    # saved in Pa, internally in GPa; this is Eeff (i.e. including 1-\nu^2)
                    self.youngProvided = toFloat(value)/1.0e9
                elif target=='X-position (um)':
                    self.xpos = toFloat(value)
                elif target=='Y-position (um)':
                    self.ypos = toFloat(value)
                elif target=='Software version':
                    self.O11['version'] = value
                elif target=='Measurement':
                    self.O11['measurement'] = value
                elif target=='Z-position (um)':
                    self.O11['zpos'] = toFloat(value)
                elif target=='Z surface (um)':
                    self.O11['zsurf'] = toFloat(value)
                elif target=='Piezo position (nm) (Measured)':
                    self.O11['piezopos'] = toFloat(value)
                elif target=='Device':
                    self.O11['device'] = value
                elif target[:10]=='SMDuration':
                    self.O11['SMDuration'] = float(value)
                elif target=='Control mode':
                    #Control mode: Displacement
                    #Control mode: Indentation
                    #Control mode: Load
                    #Control mode: Peak Load Poking
                    self.O11['mode'] = value

        #reading the protocol
        
        if self.O11['mode']=='Displacement':
            for line in f:
                if 'Loading / unloading' in line:
                    approach = float(line.strip().split('\t')[1])
                    self.protocol.append([0.0, approach])
        else:
            for line in f:
                try:                
                    if line.strip() == '':
                        break     
                    elif line[:4]=='Step':
                        break
                    slices = line.strip().replace(',', '.').split('\t')
                    num1 = float(slices[1])
                    num2 = float(slices[3])
                    self.protocol.append([float(slices[1]), float(slices[3])])
                except:
                    print('Error reading the following line:')
                    print(line)

        f.close()

    def load(self):
        f = open(self.filename,encoding='latin1')
        stopLine = 'Time (s)'
        numeric = False
        data = []
        for riga in f:
            if numeric is False:
                if riga[0:len(stopLine)] == stopLine:
                    numeric = True
            else:
                line = riga.strip().replace(',', '.').split('\t')
                # Time (s)	Load (uN)	Indentation (nm)	Cantilever (nm)	Piezo (nm)	Auxiliary
                # skip 2 = indentation and #5 auxiliary if present
                data.append([float(line[0]), float(line[1]),
                             float(line[3]), float(line[4]),float(line[2])])
        f.close()
        data = np.array(data)

        self.data['time'] = data[:, 0]
        self.data['force'] = data[:, 1]*1000.0
        self.data['deflection'] = data[:, 2]
        self.data['z'] = data[:, 3]
        self.data['indentation'] = data[:, 4]

    def toggleIndCal(self, value=False):
        for c in self:
            if c.basename == 'Calib' or c.basename == 'Indentations':
                for s in c.haystack:
                    s.active = value

class Chiaro(ChiaroBase):

    def createSegments(self):
        if self.O11['version'] == 'old':
            return self.createSegments2019()        
        time= self.data['time']
        if self.O11['mode']=='Displacement':
            nodi=[]
            nodi.append(0)
            #if displacement control, use smart mode
            signal = self.data['z']
            dy = np.abs(savgol_filter(signal,101,2,2))
            for th in range(95,100):
                threshold = np.percentile(dy,th)
                changes = find_peaks(dy,threshold)
                if len(changes[0])<10:
                    break
            for dtime in changes[0]:
                nodi.append( dtime )
            nodi.append(len(self.data['z'])-1)
        else:        
            #go safe mode
            nodi = [] 
            curtime = self.O11['SMDuration']
            #nodi.append(np.argmin((self.data['time']-curtime)**2))   
            nodi.append(0)        
            for seg in self.protocol:
                curtime += seg[1]
                nodi.append( np.argmin((self.data['time']-curtime)**2) )        
        self.nodi=nodi
        
        for i in range(len(nodi) - 1):
            if (nodi[i+1]-nodi[i])<2:
                continue
            z = self.data['z'][nodi[i]:nodi[i + 1]]
            f = self.data['force'][nodi[i]:nodi[i + 1]]
            t = self.data['time'][nodi[i]:nodi[i + 1]]
            self.append(Segment(self, z, f))
            beg = int(len(z) / 3)
            end = int(2 * len(z) / 3)
            # for future reference maybe worth adding a fit ?
            self[-1].speed = (z[end] - z[beg]) / (t[end] - t[beg])

    def createSegments2019(self, bias=30):        
        actualPos = 2
        nodi = []
        nodi.append(0)
        wait = 0
        for nextThreshold, nextTime in self.protocol:
            for j in range(actualPos, len(self.data['z'])):
                if self.data['time'][j] > wait + nextTime:
                    if self.version != 'old' or  (cross(self.data['z'][j], self.data['z'][j-1], nextThreshold, bias)) is True:
                        nodi.append(j)
                        wait = self.data['time'][j]
                        break
            actualPos = j
        nodi.append(len(self.data['z'])-1)
        self.nodi = nodi
        for i in range(len(nodi) - 1):
            z = self.data['z'][nodi[i]:nodi[i + 1]]
            f = self.data['force'][nodi[i]:nodi[i + 1]]
            t = self.data['time'][nodi[i]:nodi[i + 1]]
            self.append(Segment(self, z, f))
            beg = int(len(z) / 3)
            end = int(2 * len(z) / 3)
            # for future reference maybe worth adding a fit ?
            self[-1].speed = (z[end] - z[beg]) / (t[end] - t[beg])


class Chiaro2019(ChiaroBase):

    def createSegments(self, bias=30):        
        sign = +1
        actualPos = 2
        nodi = []
        nodi.append(0)
        wait = 0
        for nextThreshold, nextTime in self.protocol:
            for j in range(actualPos, len(self.data['z'])):
                if self.data['time'][j] > wait + nextTime:
                    if self.version != 'old' or  (cross(self.data['z'][j], self.data['z'][j-1], nextThreshold, bias)) is True:
                        nodi.append(j)
                        wait = self.data['time'][j]
                        break
            actualPos = j
        nodi.append(len(self.data['z'])-1)
        self.nodi = nodi
        for i in range(len(nodi) - 1):
            z = self.data['z'][nodi[i]:nodi[i + 1]]
            f = self.data['force'][nodi[i]:nodi[i + 1]]
            t = self.data['time'][nodi[i]:nodi[i + 1]]
            self.append(Segment(self, z, f))
            beg = int(len(z) / 3)
            end = int(2 * len(z) / 3)
            # for future reference maybe worth adding a fit ?
            self[-1].speed = (z[end] - z[beg]) / (t[end] - t[beg])


class ChiaroGenova(ChiaroBase):
    # this procedure works for old text curves from Genova, not last version
    # waiting for the feedback from Optics11 to get it corrected
    def createSegments(self):
        vs = self.protocol
        nodi = []
        nodi.append(0)
        j = 0
        nexttime = vs[j][1]
        nextvalue = vs[j][0]
        timefound = False
        valuefound = False
        for i in range(len(self.data['time'])):
            if i == len(self.data['time']) - 1:
                nodi.append(i)
            else:
                if self.data['time'][i] <= nexttime and self.data['time'][i + 1] > nexttime:
                    timefound = True
                if (self.data['z'][i] <= nextvalue and self.data['z'][i + 1] > nextvalue) or (
                        self.data['z'][i] >= nextvalue and self.data['z'][i + 1] < nextvalue):
                    valuefound = True
            if timefound and valuefound:
                nodi.append(i)
                nexttime = self.data['time'][i]
                timefound = False
                valuefound = False
                if (j + 1 == len(vs)):
                    nodi.append(len(self.data['time']) - 1)
                    break
                else:
                    j += 1
                    nexttime += vs[j][1]
                    nextvalue = vs[j][0]
        self.nodi = nodi
        for i in range(len(nodi)-1):
            z = self.data['z'][nodi[i]:nodi[i+1]]
            f = self.data['force'][nodi[i]:nodi[i+1]]
            t = self.data['time'][nodi[i]:nodi[i+1]]
            self.append(Segment(self, z, f))
            beg = int(len(z)/3)
            end = int(2*len(z)/3)
            # for future reference maybe worth adding a fit ?
            self[-1].speed = (z[end]-z[beg])/(t[end]-t[beg])

##################################
##### Nanosurf ###################
##################################


class NanoSurf(DataSet):

    def check(self):
        f = open(self.filename)
        signature = f.readline()
        f.close()
        if signature[0:9] == '#Filename':
            return True
        return False

    def header(self):
        f = open(self.filename)
        targets = ['#Cantilever=', '#Spring-Constant=',
                   '#Deflection-Sensitivity=', '#Filename=', '#SpecMap', '#SpecMode']

        def outNum(text):
            s = ''
            for c in text:
                if c.isdigit() or c in ['.', 'e', '-', '+']:
                    s += c
                else:
                    break
            return float(s)
        map_dim = [None, None]
        map_size = [None, None]
        isMap = False
        for line in f:
            if line[0:len(targets[2])] == targets[2]:  # 1.4736e-07m/V
                # NB: internal units are nm/V
                self.cantilever_lever = outNum(line[len(targets[2]):])*1e9
            elif line[0:len(targets[1])] == targets[1]:
                # NB: internal units are nm/V
                self.cantilever_k = outNum(line[len(targets[1]):])
            elif line[0:len(targets[0])] == targets[0]:
                self.cantilever_type = line[len(
                    targets[0]):].strip()  # guess the radius
                data = self.cantilever_type.strip().split('-')
                if len(data) > 1:
                    if 'um' in data[1]:
                        radius = float(data[1].replace('um', ''))*1000.0
                        self.tip_radius = radius
                    if len(data) > 2:
                        if 'um/s' in data[2]:
                            speed = float(data[1].replace('um/s', '')) * 1000.0
                            self.protocol_speed = speed
            elif line[0:len(targets[3])] == targets[3]:
                self.original_filename = line[len(targets[3]):].strip()
            elif line[0:len(targets[5])] == targets[5]:
                if line[line.find('=')+1:].strip() == 'Map':
                    isMap = True
            elif (line[0:len(targets[4])] == targets[4]) and (isMap is True):
                tp = line[line.find('-')+1:line.find('=')]
                if tp == 'Dim':
                    map_dim = line[line.find('=')+1:].split(';')
                elif tp == 'Size':
                    map_size = line[line.find('=')+1:].split(';')
                elif tp == 'CurIndex':
                    curindex = int(line[line.find('=') + 1:])
                    nx = int(map_size[0])
                    ny = int(map_size[1])
                    coordinates = []
                    dx = (float(map_dim[1]) - float(map_dim[0]))/(nx-1)
                    dy = (float(map_dim[3]) - float(map_dim[2]))/(ny-1)
                    for i in range(nx):
                        for j in range(ny):
                            coordinates.append((i*dx, j*dy))
                    self.xpos, self.ypos = coordinates[curindex]
            elif line[0] != '#':
                break
        f.close()

    def load(self):
        data = []
        dummy = True
        collected = 0
        f = open(self.filename)
        for line in f:
            if dummy is True:
                if line[0:10] == '#Spec-Data':
                    dummy = False
                    self.protocol.append(collected)
                    # Note the header line
                    # Spec-Data=Z-Axis Sensor [m];Deflection [V];Z-Axis-Out [m]
                    # Spec-Data=Z-Axis Sensor [m];Deflection [N];Z-Axis-Out [m]
                    # Units for Deflection can be either V or N !
                    self.data_channels = line[11:].strip().split(';')
                elif line[0:11] == '#Spec-Phase':
                    self.append(Segment(self))
                elif line[0:10] == '#Spec-Name':
                    if line[16:].strip() == 'forward':
                        self[-1].direction = MODE_DIRECTION_FORWARD
                    elif line[16:].strip() == 'backward':
                        self[-1].direction = MODE_DIRECTION_BACKWARD
                    else:
                        self[-1].direction = MODE_DIRECTIONS_PAUSE
                elif line[0:10] == '#Spec-Data':
                    self[-1].header = line[11:].strip()
            elif dummy is False:
                if line.strip() == '':
                    dummy = True
                else:
                    data.append(
                        [i for i in map(float, line.strip().split(';'))])
                    collected += 1
        self.protocol.append(len(data))
        f.close()
        data = np.array(data)
        # Now get as much information as possible out of the curves
        # Spec-Data=Z-Axis Sensor [m];Deflection [N];Z-Axis-Out [m]
        # mmmm, try to guess it

        check = np.abs(np.mean(data[:100, 1])*1e9)
        if check < 1000:
            self.data['force'] = data[:, 1]*1e9
        else:
            self.data['force'] = data[:, 1] * self.cantilever_lever
        self.data['z'] = data[:, 0]*1e9

    def createSegments(self):
        for i in range(len(self.protocol)-1):
            z = self.data['z'][self.protocol[i]:self.protocol[i+1]]
            f = self.data['force'][self.protocol[i]:self.protocol[i+1]]
            self[i].setData(z, f, reorder=True)


##########################
###Synthetic Hertz Data###
##########################

# Data file: .tsv file with force and displacement colums
            # only one segment, can add more
            # No header, use mother class default parameters for K, R

class Easytsv(DataSet):
    _leaf_ext = ['.tsv']

    def check(self):
        f = open(self.filename)
        l1 = f.readline().strip()
        f.close()
        if l1 == '#easy_tsv':
            return True
        else:
            return False

    def load(self):
        f = open(self.filename)
        lines = list()
        for i in range(3):  # first three lines of the file
            lines.append(f.readline().strip())  # strip removes \n
        f.close()
        # K value needed by program
        self.cantilever_k = float(lines[1][lines[1].find(':')+1:].strip())
        # R value needed by program
        self.tip_radius = float(lines[2][lines[2].find(':')+1:].strip())
        data = np.loadtxt(self.filename, delimiter='\t', skiprows=4)
        self.data['force'] = data[:, 1]
        self.data['z'] = data[:, 0]

    def createSegments(self):
        self.append(Segment(self))
        self[0].setData(self.data['z'], self.data['force'])

class Jpkcurve(DataSet):
    _leaf_ext = ['.txt']

    def load(self):
        f = afmformats.load_data(self.filename)
        # inspect the columns
        # print(f[0].columns)

        fd = afmformats.mod_force_distance.AFMForceDistance(
            f[self.curveid]._raw_data, f[self.curveid].metadata, diskcache=False)

        self._segmentend=len(fd.appr['force'])
        self.data['force'] = np.append(fd.appr['force']*1e9, fd.retr['force']*1e9)
        self.data['z'] = np.append(-1.0*(fd.appr['height (measured)']*1e9), -1.0*(fd.retr['height (measured)']*1e9)) #flip z
        self.data['time']=np.append(fd.appr['time'], fd.retr['time'])
        metadata = fd.metadata
        # print(fd.metadata)
        self.cantilever_k = metadata['spring constant']
        self.tip_radius = 1.0  #nm (user input)

    def createSegments(self):
        self.append(Segment(self, self.data['z'][self._segmentend:], self.data['force'][self._segmentend:]))
        self.append(Segment(self, self.data['z'][:self._segmentend], self.data['force'][:self._segmentend]))

class JPKExport(DataSet):
    _leaf_ext = ['.txt']

    def is_leaf(self):
        return False

    def __init__(self, filename=None, parent=None):
        super().__init__(filename, parent)
        if self._filehandler.is_file() is True:
            f = afmformats.load_data(filename)
            for i in range(len(f)):
                newleaf = Jpk(filename,self)
                newleaf.curveid = i
                self.append(newleaf)
    _leaf_ext = ['.txt']

    def check(self):
        f = open(self.filename)
        l1 = f.readline().strip()
        f.close()
        if l1[0] == '#':
            return True
        else:
            return False

    def load(self):
        f = open(self.filename)
        lines = list()
        for i in range(3):  # first three lines of the file
            lines.append(f.readline().strip())  # strip removes \n
        f.close()
        # K value needed by program
        self.cantilever_k = float(lines[1][lines[1].find(':')+1:].strip())
        # R value needed by program
        #self.tip_radius = float(lines[2][lines[2].find(':')+1:].strip())
        data = np.loadtxt(self.filename, delimiter='\t', skiprows=4)
        self.data['force'] = data[:, 1]
        self.data['z'] = data[:, 0]

    def createSegments(self):
        self.append(Segment(self))
        self[0].setData(self.data['z'], self.data['force'])


class Jpk(DataSet):
    _leaf_ext = ['.jpk-force']

    def load(self):
        f = afmformats.load_data(self.filename)
        # inspect the columns
        # print(f[0].columns)

        fd = afmformats.mod_force_distance.AFMForceDistance(
            f[self.curveid]._raw_data, f[self.curveid].metadata, diskcache=False)

        self._segmentend=len(fd.appr['force'])
        self.data['force'] = np.append(fd.appr['force']*1e9, fd.retr['force']*1e9)
        self.data['z'] = np.append(-1.0*(fd.appr['height (measured)']*1e9), -1.0*(fd.retr['height (measured)']*1e9)) #flip z
        self.data['time']=np.append(fd.appr['time'], fd.retr['time'])
        metadata = fd.metadata
        # print(fd.metadata)
        self.cantilever_k = metadata['spring constant']
        self.tip_radius = 1.0  #nm (user input)

    def createSegments(self):
        self.append(Segment(self, self.data['z'][self._segmentend:], self.data['force'][self._segmentend:]))
        self.append(Segment(self, self.data['z'][:self._segmentend], self.data['force'][:self._segmentend]))

class JpkForceMap(DataSet):
    _leaf_ext = ['.jpk-force-map']

    def is_leaf(self):
        return False

    def __init__(self, filename=None, parent=None):
        super().__init__(filename, parent)
        if self._filehandler.is_file() is True:
            f = afmformats.load_data(filename)
            for i in range(len(f)):
                newleaf = Jpk(filename,self)
                newleaf.curveid = i
                self.append(newleaf)