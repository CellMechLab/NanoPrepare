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
    def getCurves(self):
        haystack=[]
        for i in range(self.rowCount()):
            c = self.child(i)
            if c.isCurve is True:
                haystack.append(c) 
            else:
                for h in c.getCurves():
                    haystack.append(h)
        return haystack
        
    def attach(self,filename,isdir=False):
        if isdir is True:
            row = MVcurve(filename,self.proxy)                    
            self.appendRow([row,*emptyItems])
        else:     
            try:     
                totest = self.proxy.opener(Path(filename))
                if totest.isMultiple() is False:
                    row = MVcurve(Path(filename),self.proxy)
                    addItems = [QStandardItem(str(row.curve.parameters['k']))]
                    addItems.append(QStandardItem(str(row.curve.tip['geometry'])))
                    addItems.append(QStandardItem(row.curve.tip['parameter'] +': '+ str(row.curve.tip['value'])+' '+row.curve.tip['unit']))
                    addItems.append(QStandardItem(str(len(row.curve.segments))))
                    self.appendRow([row,*addItems])
                else:
                    for number in totest:
                        row = MVcurve(Path(filename),self.proxy,number)
                        addItems = [QStandardItem(str(row.curve.parameters['k']))]
                        addItems.append(QStandardItem(str(row.curve.tip['geometry'])))
                        addItems.append(QStandardItem(row.curve.tip['parameter'] +': '+ str(row.curve.tip['value'])+' '+row.curve.tip['unit']))
                        addItems.append(QStandardItem(str(len(row.curve.segments))))
                        self.appendRow([row,*addItems])
                return True
            except NotValidFile:
                return False
        

class MVcurve(QStandardItem,MVbase):
    def __init__(self,filename,proxy,number=False):    
        filename = Path(filename)    
        super().__init__(filename.name)
        self.isCurve = False
        self.proxy = proxy
        self.number=number
        self.line=None
        if filename.is_dir():
            for ddir in filename.iterdir():
                self.attach(ddir,ddir.is_dir())
        else:
            self.isCurve = True
            self.createCurve(filename)

    def createCurve(self,path):        
        if self.proxy.EXT != '*' and path.suffix != self.proxy.EXT :
            raise NotValidFile('Extension not valid')
        chiaro = self.proxy.opener(path)
        if chiaro.check() is False:
            raise NotValidFile('This does not look like an Optics11 file')   
        self.setCheckable(True)
        self.setCheckState( Qt.CheckState.Checked )        
        self.curve = chiaro.open()    
            
                

class MVexperiment(QStandardItemModel,MVbase):
    def __init__(self,root=None):        
        super().__init__()
        self.setHorizontalHeaderLabels(['Filename','k','Tip','Size','Segments'])
        self.proxy = None
        self.setProxy()
        self.haystack=[]
        if root is not None:
            self.createTree(root)
            
    def pileup(self):
        root = self.invisibleRootItem() 
        self.haystack=[]
        for i in range(root.rowCount()):
            c = root.child(i)
            if c.isCurve is True:
                self.haystack.append(c) 
            else:
                for h in c.getCurves():
                    self.haystack.append(h)
    
    def setProxy(self,mode='Optics11'):
        if mode == 'Optics11':
            import openers.chiaro as O11    
            self.proxy = O11
        elif mode=='AFM':
            import openers.afm as afm    
            self.proxy = afm

    def createTree(self,root):
        root = Path(root) 
        if root.is_file():
            self.attach(root)
        else:    
            for ddir in Path(root).iterdir():
                self.attach(ddir,ddir.is_dir())        