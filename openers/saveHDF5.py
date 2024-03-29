


class saveHDF5(object):
    def __init__(self,fname) -> None:
        self.filename = fname
        self.selectedsegment = 0
        
    def addCurve(self, curve):
        pass
    
    def setSegment(self, number):
        self.selectedsegment = number
        
    def save(self):
        pass