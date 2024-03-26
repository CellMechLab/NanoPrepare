import sys
from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pyqtgraph as pg

from pathlib import Path
from openers.chiaro import opener

EXT = '.txt'

class NotValidFile(Exception):
    """ my custom exception class """

class MVbase(object):
    def attach(self,filename):     
        try:     
            row = MVcurve(Path(filename))
            self.appendRow([row,QStandardItem(str(row.curve.parameters['k'])),QStandardItem(str(row.curve.tip['value']))])
        except NotValidFile:
            pass
        except:
            raise       

class MVcurve(QStandardItem,MVbase):
    def __init__(self,filename):    
        filename = Path(filename)    
        super().__init__(filename.name)
        self.isCurve = False
        self.createCurve(filename)

    def createCurve(self,path):        
        if path.is_file():
            if path.suffix != EXT:
                raise NotValidFile('Extension not valid')
            chiaro = opener(path)
            if chiaro.check() is False:
                raise NotValidFile('This does not look like an Optics11 file')   
            self.isCurve = True
            self.setCheckable(True)
            self.setCheckState( Qt.CheckState.Checked )        
            self.curve = chiaro.open()    
        else:
            for ddir in path.iterdir():
                if ddir.is_dir() is True:
                    row = MVcurve(ddir)                    
                    self.appendRow([row,QStandardItem(),QStandardItem()])
                elif ddir.is_file() is True:
                    self.attach(ddir)                      

class MVexperiment(QStandardItemModel,MVbase):

    def __init__(self,root=None):        
        super().__init__()
        self.setHorizontalHeaderLabels(['Filename','k','R'])
        if root is not None:
            self.createTree(root)

    def createTree(self,root):         
        for ddir in Path(root).iterdir():
            if ddir.is_dir() is True:
                row = MVcurve(ddir)                    
                self.appendRow([row,QStandardItem(),QStandardItem()])
            elif ddir.is_file() is True:
                self.attach(ddir)
        