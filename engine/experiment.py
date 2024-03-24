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

    def __init__(self,root):
        named = Path(root)
        super().__init__()
        self.root = root
        self.setHorizontalHeaderLabels(['Filename','k','R'])
        self.createTree(named)

    def createTree(self,root):         
        for ddir in root.iterdir():
            if ddir.is_dir() is True:
                row = MVcurve(ddir)                    
                self.appendRow([row,QStandardItem(),QStandardItem()])
            elif ddir.is_file() is True:
                if ddir.suffix == EXT:
                    row = MVcurve(ddir)
                    #box = QStandardItem()                    
                    self.appendRow([row,QStandardItem('22'),QStandardItem('12')])
                    #self.appendRow(row)
        