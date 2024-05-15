#import the main panels structure, required
from PySide6 import QtGui, QtWidgets, QtCore
from ..panels import boxPanel
#import here your procedure-specific modules, no requirements (numpy as an example)
import numpy as np
from magicgui.widgets import  FloatSpinBox

#Set here the details of the procedure
NAME = 'Threshold' #Name, please keep it short as it will appear in the combo box of the user interface
DESCRIPTION = 'Screen curves by setting the threshold (minimum max force reached during the segment)' #Free text
DOI = '' #set a DOI of a publication you want/suggest to be cited, empty if no reference
PARAMETERS = {} #set a dictionary with the fitting model parameters. For example,
#for a simple hertz model this would be PARAMETERS = {'E [Pa]':"Young's modulus"}

# Create your filter class by extending the main one
# Additional methods can be created, if required
class Screener(boxPanel):
    def create(self):
        # This function is required and describes the form to be created in the user interface 
        # The last value is the initial value of the field; currently 3 types are supported: int, float and combo
        # Parameters can be used as seeds or proper parameters (e.g. indentation depth ?) 
        self.addParameter('Threshold',FloatSpinBox(value=1, name='threshold', label='Force threshold [nN]',min=-1,max=1000))
        
    def calculate(self, x,y):
        # This function gets the current x and y and returns whether to keep the curve or not.
        threshold = self.getValue('Threshold')*1e-9
        if np.max(y)>threshold:
            return True
        else:
            return False