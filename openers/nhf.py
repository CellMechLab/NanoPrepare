import openers._skeleton as skeleton
import numpy as np
import h5py

NAME = 'NHF Nanosurf basic opener'
EXT = '.nhf'

class opener(skeleton.prepare_opener):
    def isMultiple(self):
        data=[]
        innerattr = []
        with h5py.File(self.filename, 'r') as f:
            subgroup = f['/group_0000/']
            attributes = {key: subgroup.attrs[key] for key in subgroup.attrs}
        x,y = attributes['rect_axis_size']
        self.number = x*y
        return True

    def open(self,number=False):

        with h5py.File(self.filename, 'r') as f:
            general_fw = f['/group_0000/']
            gen_att = {key: general_fw.attrs[key] for key in general_fw.attrs}
            xdata = f['/group_0000/dataset_0000/'][:]
            ydata = f['/group_0000/dataset_0001/'][:]            
            
            subgroup = f['/group_0000/subgroup_0000/']
            attributes = {key: subgroup.attrs[key] for key in subgroup.attrs}
            T = f['/group_0000/subgroup_0000/dataset_0011'][:]
            Zdataset = f['/group_0000/subgroup_0000/dataset_0004']
            Z = Zdataset[:]*-1
            coeZ = (Zdataset.attrs['signal_calibration_max']-Zdataset.attrs['signal_calibration_min'])/(Zdataset.attrs['signal_minmax'][1]-Zdataset.attrs['signal_minmax'][0])
            Ddataset = f['/group_0000/subgroup_0000/dataset_0003']
            D = Ddataset[:]
            coeDV = (Ddataset.attrs['signal_calibration_max']-Ddataset.attrs['signal_calibration_min'])/(Ddataset.attrs['signal_minmax'][1]-Ddataset.attrs['signal_minmax'][0])
            stop = f['/group_0000/subgroup_0000/dataset_0001']
            
            istart = np.sum(stop[:number-1])
            #istart = istart+2 if istart>0 else 0            
            iend = istart+stop[number-1]
            
            k = gen_att['spm_probe_calibration_spring_constant']
            self.curve.parameters['k'] = k
            invols = gen_att['spm_probe_calibration_deflection_sensitivity'] 
            self.curve.parameters['x'] = xdata[number]
            self.curve.parameters['y'] = ydata[number]            
            coeD = coeDV*invols
        
        
        
        data = np.transpose(np.vstack([dset[istart:iend] for dset in [T,Z*coeZ,D*coeD]]))
        
        self.curve.channels = ['Time','Z Position [m]','Deflection [m]']
        self.curve.idTime = 0
        self.curve.idForce = 2
        self.curve.idZ = 1
        self.curve.isDeflection = True
        self.curve.tip['value']=1e-5
        self.curve.data=data
        
        self.curve.attach(self.curve.data)

        
        return self.curve