
import h5py

class saveHDF5(object):
    def __init__(self,fname) -> None:
        self.filename = fname
        self.selectedsegment = 0
        self.curves=[]
        
    def addCurve(self, curve):
        self.curves.append(curve)
    
    def setSegment(self, number):
        self.selectedsegment = number
        
    def save(self):
        hd = h5py.File(self.filename,'w')
        hd.attrs['selectedSegment']=self.selectedsegment
        hd.attrs['curves']=len(self.curves)
        i=0
        for curve in self.curves:
            name = 'curve'+str(i)
            i+=1
            cv = hd.create_group(name)
            cv.attrs['filename']=str(curve.filename)
            cv.attrs['spring_constant']=curve.parameters['k']
            cv.attrs['x-position']=curve.parameters['x']
            cv.attrs['y-position']=curve.parameters['y']
            tip = cv.create_group('tip')
            for key in curve.tip:
                tip.attrs[key]=curve.tip[key]
            z,f=curve.segments[self.selectedsegment].getCurve()
            cv.create_dataset('Z',data=z)
            cv.create_dataset('F',data=f)
        hd.close()