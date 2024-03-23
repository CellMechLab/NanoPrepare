
import openers._skeleton as skeleton
import numpy as np

NAME = 'Chiaro Optics11'
EXT = '.txt'

class opener(skeleton.prepare_opener):
    def check(self):
        self.version = None

    def parse(self):
        f = open(self.filename)
        for riga in f:
            if riga.startswith('Time (s)'):
                channels = riga.strip().split('\t')
                for i in range(len(channels)):
                    if channels[i].startswith('Time'):
                        self.idTime = i
                    elif channels[i].startswith('Load'):
                        self.idForce = i
                    elif channels[i].startswith('Piezo'):
                        self.idZ = i
                break
            else:
                if riga.startswith('X-position'):
                    self.parameters['x']=float(riga.strip().split('\t')[1])
                elif riga.startswith('Y-position'):
                    self.parameters['y']=float(riga.strip().split('\t')[1])
                elif riga.startswith('k (N/m)'):
                    self.parameters['k']=float(riga.strip().split('\t')[1])
                elif riga.startswith('Tip radius'):
                    self.tip['value']=float(riga.strip().split('\t')[1])
                elif riga.startswith('Control mode'):
                    self.parameters['control']=riga.strip().split(':')[1]
                elif riga.startswith('Measurement'):
                    self.parameters['measurement']=riga.strip().split(':')[1]
                elif riga.startswith('Software'):
                    self.parameters['version']=riga.strip().split(':')[1].strip()
                elif riga.startswith('SMDuration'):
                    self.parameters['SMDuration']=float(riga.strip().split(' ')[-1])
        data = []
        for riga in f:
            elements = riga.strip().split('\t')
            if len(elements) == len(channels):
                values = [float(x) for x in elements]
                data.append(values)
        self.data = np.array(data)
        f.close()