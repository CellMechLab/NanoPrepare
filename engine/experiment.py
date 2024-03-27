import sys
from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pyqtgraph as pg

from pathlib import Path

class NotValidFile(Exception):
    """ my custom exception class """

emptyItems=[QStandardItem() for _ in range(4)]
class MVbase(object):
    def attach(self,filename):     
        try:     
            row = MVcurve(Path(filename))
            addItems = [QStandardItem(str(row.curve.parameters['k']))]
            addItems.append(QStandardItem(str(row.curve.tip['geometry'])))
            addItems.append(QStandardItem(row.curve.tip['parameter'] +': '+ str(row.curve.tip['value'])+' '+row.curve.tip['unit']))
            addItems.append(QStandardItem(str(len(row.curve.segments))))
            self.appendRow([row,*addItems])
            return True
        except NotValidFile:
            return False
        

class MVcurve(QStandardItem,MVbase):
    def __init__(self,filename):    
        filename = Path(filename)    
        super().__init__(filename.name)
        self.isCurve = False
        self.createCurve(filename)

    def createCurve(self,path):        
        import openers.chiaro as proxy
        if path.is_file():
            if path.suffix != proxy.EXT :
                raise NotValidFile('Extension not valid')
            chiaro = proxy.opener(path)
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
                    self.appendRow([row,*emptyItems])
                elif ddir.is_file() is True:
                    self.attach(ddir)                      


class MVexperiment(QStandardItemModel,MVbase):

    def __init__(self,root=None):        
        super().__init__()
        self.setHorizontalHeaderLabels(['Filename','k','Tip','Size','Segments'])
        if root is not None:
            self.createTree(root)

    def createTree(self,root):         
        for ddir in Path(root).iterdir():
            if ddir.is_dir() is True:
                row = MVcurve(ddir)                    
                self.appendRow([row,*emptyItems])
            elif ddir.is_file() is True:
                self.attach(ddir)
        