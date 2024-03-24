
import openers._skeleton as skeleton
import numpy as np

NAME = 'Chiaro Optics11'
EXT = '.txt'

class opener(skeleton.prepare_opener):
    def check(self):
        self.version = None

    def open(self):
        self.parse()
        self.createSegments()
        return self.curve

    def createSegments(self):
        pass

    def parse(self):
        f = open(self.filename)
        for riga in f:
            if riga.startswith('Time (s)'):
                self.curve.channels = riga.strip().split('\t')
                for i in range(len(self.curve.channels)):
                    if self.curve.channels[i].startswith('Time'):
                        self.curve.idTime = i
                    elif self.curve.channels[i].startswith('Load'):
                        self.curve.idForce = i
                    elif self.curve.channels[i].startswith('Piezo'):
                        self.curve.idZ = i
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
        self.curve.data = np.array(data)
        f.close()