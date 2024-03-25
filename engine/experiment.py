import sys
from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pyqtgraph as pg

from pathlib import Path
from openers.chiaro import opener

EXT = '.txt'

class MVcurve(QStandardItem):

    def __init__(self,filename):
        super().__init__(filename.name)
        self.createCurve(filename)
        self.isCurve = False

    def createCurve(self,path):        
        if path.is_file():
            chiaro = opener(path)
            if chiaro.check() is False:
                return False            
            self.isCurve = True
            self.setCheckable(True)
            self.setCheckState(True)        
            self.curve = opener.open()    
        else:
            for ddir in path.iterdir():
                if ddir.is_dir() is True:
                    row = MVcurve(ddir)                    
                    self.appendRow([row,QStandardItem(),QStandardItem()])
                elif ddir.is_file() is True:
                    if ddir.suffix == EXT:
                        row = MVcurve(ddir)
                        self.appendRow([row,QStandardItem('k=22'),QStandardItem('R=12')])
                        #self.appendRow(row)

class MVexperiment(QStandardItemModel):

    def __init__(self,root=None):        
        super().__init__()
        self.setHorizontalHeaderLabels(['Filename','k','R'])
        if root is not None:
            self.createTree(Path(root))

    def attach(self,filename):        
        row = MVcurve(filename)
        if row is not False:
            self.appendRow([row,QStandardItem(row.curve.parameters['k']),QStandardItem(row.curve.tip['value'])])

    def createTree(self,root):         
        for ddir in root.iterdir():
            if ddir.is_dir() is True:
                row = MVcurve(ddir)                    
                self.appendRow([row,QStandardItem(),QStandardItem()])
            elif ddir.is_file() is True:
                if ddir.suffix == EXT:
                    self.attach(ddir)
        