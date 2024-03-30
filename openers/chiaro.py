
import openers._skeleton as skeleton
import numpy as np

NAME = 'Chiaro Optics11'
EXT = '.txt'

def cross(x1, x2, th, dth):
    th1 = th+dth
    th2 = th-dth
    if np.sign(x1-th1) != np.sign(x2-th1):
        return True
    if np.sign(x1-th2) != np.sign(x2-th2):
        return True
    return False

def getNodes(curve,mode='safe',value=30*1e-9):
        if mode=='safe':
            nodi = [] 
            curtime = curve.parameters['SMDuration']
            #nodi.append(np.argmin((self.data['time']-curtime)**2))   
            nodi.append(0)        
            time = curve.data[:,curve.idTime]
            for seg in curve.protocols:
                curtime += seg[1]
                nodi.append( np.argmin((time-curtime)**2) )     
        elif mode=='euristic':
            sign = +1
            nodi = []
            nodi.append(0)
            wait = 0
            Z = curve.data[:,curve.idZ]
            T = curve.data[:,curve.idTime]
            actualPos = 2
            for nextThreshold, nextTime in curve.protocols:
                for j in range(actualPos, len(Z)):
                    if T[j] > wait + nextTime:
                        crossp = Z[j-1]>=nextThreshold*1e-9 and Z[j]<nextThreshold*1e-9
                        crossm = Z[j-1]<=nextThreshold*1e-9 and Z[j]>nextThreshold*1e-9
                        if crossp or crossm:
                            nodi.append(j)
                            actualPos = j
                            wait = T[j]
                            break
            nodi.append(len(Z)-1)   
        else:
            pass
        return nodi

class opener(skeleton.prepare_opener):
    def check(self):
        f = open(self.filename)
        riga = f.readline()
        f.close()
        return riga.startswith('Date')

    def open(self):
        self.parse()
        self.getProtocols()
        self.createSegments()
        return self.curve
    
    def getProtocols(self):
        protocols=[]
        f = open(self.filename)
        next = False
        for riga in f:
            if riga.startswith('Profile') or riga.startswith('Piezo Indentation'):
                next = True
            elif next is True:
                if riga.startswith('D'):
                    elements = riga.strip().split('\t')
                    protocols.append([float(elements[1]),float(elements[3])])
                else:
                    break
        f.close()
        self.curve.protocols = protocols

    def createSegments(self):
        nodi = getNodes(self.curve,'safe')
        for i in range(len(nodi) - 1):
            if (nodi[i+1]-nodi[i])<2:
                continue
            self.curve.attach(self.curve.data[nodi[i]:nodi[i + 1],:])

    def parse(self):
        #specific parameters
        self.curve.parameters['SMDuration']=0.0

        f = open(self.filename)
        for riga in f:
            if riga.startswith('Time (s)'):
                self.curve.channels = riga.strip().split('\t')
                #Time (s)	Load (uN)	Indentation (nm)	Cantilever (nm)	Piezo (nm)	Auxiliary
                self.multipliers = np.ones(len(self.curve.channels))
                for i in range(len(self.curve.channels)):
                    if self.curve.channels[i].startswith('Time'):
                        self.curve.idTime = i
                    elif self.curve.channels[i].startswith('Load'):
                        self.curve.idForce = i
                    elif self.curve.channels[i].startswith('Piezo'):
                        self.curve.idZ = i
                    if '(nm)' in self.curve.channels[i]:
                        self.multipliers[i]=1e-9
                    elif 'uN' in self.curve.channels[i]:
                        self.multipliers[i]=1e-6
                break
            else:
                if riga.startswith('X-position'):
                    self.curve.parameters['x']=float(riga.strip().split('\t')[1])
                elif riga.startswith('Y-position'):
                    self.curve.parameters['y']=float(riga.strip().split('\t')[1])
                elif riga.startswith('k (N/m)'):
                    self.curve.parameters['k']=float(riga.strip().split('\t')[1])
                elif riga.startswith('Tip radius'):
                    self.curve.tip['value']=float(riga.strip().split('\t')[1])
                elif riga.startswith('Control mode'):
                    self.curve.parameters['control']=riga.strip().split(':')[1]
                elif riga.startswith('Measurement'):
                    self.curve.parameters['measurement']=riga.strip().split(':')[1]
                elif riga.startswith('Software'):
                    self.curve.parameters['version']=riga.strip().split(':')[1].strip()
                elif riga.startswith('SMDuration'):
                    self.curve.parameters['SMDuration']=float(riga.strip().split(' ')[-1])
        data = []
        for riga in f:
            elements = riga.strip().split('\t')
            if len(elements) == len(self.curve.channels):
                values = [float(x) for x in elements]
                data.append(values)
        self.curve.data = np.array(data)*self.multipliers
        f.close()