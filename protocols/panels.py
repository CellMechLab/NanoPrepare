from PySide6 import QtGui, QtWidgets, QtCore
from importlib import import_module
from magicgui.widgets import Label
            
class boxPanel:  # Contact point class
    def __init__(self):
        self._parameters = {}
        self.create()

    def create(self):
        #This function contains the list of parameters to be added
        pass

    def do(self, x,y,curve=None):
        #This is the main engine, performing the calculation
        self.curve = curve
        return self.calculate(x,y)

    def calculate(self, x,y):
        # this does the job, please do overload it!
        pass

    def disconnect(self):
        #disconnect the callback from the parameters
        for p in self._parameters.values():
            p.changed.disconnect()

    def connect(self, callback):
        #connect the callback to the parameters
        for p in self._parameters.values():
            p.changed.connect(callback)

    def getValue(self,name):
        return self._parameters[name].value

    def addParameter(self,name, widget):
        self._parameters[name] = widget

    def createUI(self, layout):
        while(layout.rowCount()>0):
            layout.removeRow(0)
        for widget in self._parameters.values():
            layout.addRow(widget.label, widget.native)