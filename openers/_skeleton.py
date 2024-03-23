import os

tips = {
    'sphere':{'geometry':'sphere','parameter':'Radius','unit':'nm','value':0.0},
    'cylinder':{'geometry':'cylinder','parameter':'Radius','unit':'nm','value':0.0},
    'cone':{'geometry':'cone','parameter':'Angle','unit':'deg','value':0.0},
    'pyramid':{'geometry':'pyramid','parameter':'Angle','unit':'deg','value':0.0},
    'other':{'geometry':'other','parameter':'Unknown','unit':'au','value':0.0}
}


class prepare_opener(object):
    def __init__(self,file_path) -> None:
        self.filename = file_path
        self.dir , self.basename = os.path.split(file_path)
        self.data = None
        self.segments = None
        self.tip = tips['sphere']
        self.parameters={'k':None,'x':None,'y':None}
        self.idTime=None
        self.idForce=None
        self.idZ = None
        self.isDeflection=False
        return self.check()
        
    def check(self):
        return True
    
    def open(self):
        self.parse()