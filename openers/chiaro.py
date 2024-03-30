
import openers._skeleton as skeleton
import numpy as np

NAME = 'Chiaro Optics11'
EXT = '.txt'

def getNodes(curve,mode='safe'):
        if mode=='safe':
            nodi = [] 
            curtime = curve.parameters['SMDuration']
            #nodi.append(np.argmin((self.data['time']-curtime)**2))   
            nodi.append(0)        
            time = curve.data[:,curve.idTime]
            for seg in curve.protocols:
                curtime += seg[1]
                nodi.append( np.argmin((time-curtime)**2) )        
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