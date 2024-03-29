#import the main panels structure, required
from ..panels import boxPanel
#import here your procedure-specific modules, no requirements (numpy as an example)
import numpy as np
from magicgui.widgets import  FloatSlider

#Set here the details of the procedure
NAME = 'Screening procedure' #Name, please keep it short as it will appear in the combo box of the user interface
DESCRIPTION = 'Screen curves through ...' #Free text
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
        self.addParameter('poisson',FloatSlider(value=0.5, name='poisson', label='Poisson ratio',min=-1,max=0.5))

    def calculate(self, x,y):
        # This function gets the current x and y and returns whether to keep the curve or not.
        today = 'not bad day'
        if today is True:
            return True
        else:
            return False