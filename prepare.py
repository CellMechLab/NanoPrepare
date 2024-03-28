import sys,os
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog, QFormLayout
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QDir, QModelIndex, QItemSelectionModel
from engine.mainwindow import UI
from engine.tipselection import PopupWindow as tipPopup
import pyqtgraph as pg
from engine.experiment import MVexperiment
from pathlib import Path
import protocols.screening


class engine(object):
    def __init__(self) -> None:
        #set up the ui and the signal/slot connection
        self.ui = UI()
        self.DISABLE = False
        self.ui.openfile.clicked.connect(self.open_files)
        self.ui.openfolder.clicked.connect(self.open_folder)
        self.ui.toggle_button.clicked.connect(self.toggle_button_clicked)
        self.ui.saveas.clicked.connect(self.saveas_button_clicked)
        #the model contains the tree of curve objects and is used for the treeview
        self.model = MVexperiment()
        self.ui.filelist.setModel(self.model)
        self.model.rowsInserted.connect(self.setCurve) #add features while populating
        self.resizeView()
        self.ui.filelist.expanded.connect(self.resizeView)
        self.model.itemChanged.connect(self.changeDetected) #check for clicks on the checkbox       
        self.ui.filelist.selectionModel().selectionChanged.connect(self.highlight) #manage the selection
        self.ui.segmentSlider.valueChanged.connect(self.refreshView) #change the active segment and refresh the view
        self.ui.tipselect.clicked.connect(self.setTip)
        self.ui.slider.valueChanged.connect(self.slideCurves)
        self.loadPlugins()
        self.ui.sel_screen.currentIndexChanged.connect(self.screenSelected) #populate the screening area on demand
        
    def toggle_button_clicked(self):
        if self.ui.toggle_button.isChecked():
            self.ui.toggle_button.setText("AFM")
            self.model.setProxy('AFM')
            self.ui.toggle_button.setStyleSheet('color: red;')
        else:
            self.ui.toggle_button.setText("Optics11")
            self.model.setProxy('Optics11')
            self.ui.toggle_button.setStyleSheet('color: green;')
            
    def saveas_button_clicked(self):
        if self.ui.saveas.isChecked():
            self.ui.saveas.setText("HDF5")
            self.model.setProxy('HDF5')
            self.ui.saveas.setStyleSheet('color: red;')
        else:
            self.ui.saveas.setText("JSON")
            self.model.setProxy('JSON')
            self.ui.saveas.setStyleSheet('color: green;')
            
    def highlight(self,new,old): #highlights the current xcurve and plots it in the right panel
        self.DISABLE = True
        if old.isEmpty() is False:
            oldnum = old.first().indexes()[0].row()
            rowold = self.model.item(oldnum,0)
            color = rowold.line.opts['pen'].color().name()
            rowold.line.setPen(color=color,width=1)
        newnum = new.first().indexes()[0].row()
        self.ui.slider.setValue(newnum)
        rownew = self.model.item(newnum,0)
        color = rownew.line.opts['pen'].color().name()
        rownew.line.setPen(color=color,width=3)
        self.ui.rightcurve.setData(*rownew.line.getData())
        self.DISABLE = False

    def getRow(self,rowindex):
        return self.model.itemFromIndex(self.model.index(rowindex,0))
    
    def slideCurves(self,value):
        if self.DISABLE is False:
            self.ui.filelist.selectionModel().select(self.model.index(value,0) ,QItemSelectionModel.SelectionFlag.SelectCurrent)
        
    def lineclick(self,line): #line-click selection
        self.ui.filelist.selectionModel().select(line.parentitem.index(),QItemSelectionModel.SelectionFlag.SelectCurrent )
        
    def setCurve(self,parent,first,last): #adds a curve to the model for each file added to it
        row = self.model.itemFromIndex(self.model.index(first,0))
        curSeg = self.ui.segmentSlider.value()
        x,y = row.curve.segments[curSeg].getCurve()
        row.line= pg.PlotCurveItem(x,y,pen='g')
        row.line.setClickable(True)
        self.ui.graphleft.addItem(row.line)
        row.line.parentitem = row
        row.line.sigClicked.connect(self.lineclick)
        
    def open_folder(self): #opens and browses a folder
        fname = QFileDialog.getExistingDirectory(self.ui, 'Select the root dir', self.ui.wdir.text() )
        if fname == '' or fname is None or fname[0] == '':
            return
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        self.ui.wdir.setText(fname)
        self.model.createTree(fname)
        self.resizeView()
        self.refreshView()
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        
    def open_files(self): #opens a bunch of files
        filename = QFileDialog.getOpenFileNames(self.ui, 'Select the file', self.ui.wdir.text())
        if filename == '' or filename is None or filename[0] == '' or len(filename[0])==0:
            return
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        for fname in filename[0]:
            fname = Path(fname)
            if self.model.attach(fname) is True:
                self.ui.wdir.setText(str(fname.parents[0]))
        self.resizeView()
        self.refreshView()
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)        
            #popup = PopupWindow(self.ui)
            #if popup.exec() == QDialog.DialogCode.Accepted:
            #    selected_value = popup.on_button2_clicked()
            #    print(selected_value)    

        
    def refreshView(self,curSeg=None):
        self.ui.nfiles.setText(str( int( (self.model.rowCount() ) )))
        self.ui.slider.setMaximum(self.model.rowCount()-1)
        if curSeg is None:
            nsegs = 0
            for i in range(self.model.rowCount()):
                row = self.model.itemFromIndex(self.model.index(i,0))
                nsegs = max(nsegs,len(row.curve.segments))
            self.ui.segmentSlider.setMaximum(nsegs-1)
        else:
            for i in range(self.model.rowCount()):
                row = self.model.itemFromIndex(self.model.index(i,0))
                row.line.setData(*row.curve.segments[curSeg].getCurve())
            self.ui.rightcurve.setData([],[])
            sel = self.ui.filelist.selectedIndexes()[0]
            row = self.model.itemFromIndex(self.model.index(sel.row(),0))
            self.ui.rightcurve.setData(*row.line.getData())

    def resizeView(self):
        self.ui.filelist.resizeColumnToContents(0)
        
    def changeDetected(self,item): #manages changes to the view
        if item.column()==0:            
            width = item.line.opts['pen'].width()
            if item.checkState() == Qt.CheckState.Checked:       
                item.line.setPen(color='g',width=width)
            else:
                item.line.setPen(color='r',width=width)
        elif item.column()==2:
            obj = self.getRow(item.row())
            obj.curve.parameters['k']=float(item.text())
        elif item.column()==2:
            pass
        elif item.column()==3:
            pass
        
    def loadPlugins(self):
        data = protocols.screening.list()
        self._plugin_screen = list(data.keys())
        for l in data.values():
            self.ui.sel_screen.addItem(l)
            
    def screenSelected(self,fid):
        if fid == 0:
            return
        layout = self.ui.box_cp.layout()
        if layout is None:
            layout = QFormLayout()
        self._screen = protocols.screening.get(self._plugin_screen[fid-1])
        
        self._screen.createUI(layout)
        self._screen.connect(self.calc)
        self.ui.box_cp.setLayout(layout)
        self.calc()
        
    def calc(self):
        for i in range(self.model.rowCount()):
            row = self.model.itemFromIndex(self.model.index(i,0))
            if self._screen.do(*row.line.getData()) is False:
                row.setCheckState(Qt.CheckState.Unchecked)
            
    def setTip(self):
        popup = tipPopup(self.ui)
        if popup.exec() == QDialog.DialogCode.Accepted:
            geometry,value = popup.on_ok_clicked()
            for i in range(self.model.rowCount()):
                row = self.model.itemFromIndex(self.model.index(i,2))
                obj = self.getRow(i)
                obj.curve.tip['geometry']=geometry
                if geometry=='sphere' or geometry=='cylinder':
                    obj.curve.tip['parameter']='Radius'
                    obj.curve.tip['unit']='um'
                else:
                    obj.curve.tip['parameter']='Angle'
                    obj.curve.tip['unit']='deg'
                obj.curve.tip['value']=value
                row.setText(geometry)
                row = self.model.itemFromIndex(self.model.index(i,3))
                row.setText(f"{obj.curve.tip['parameter']}: {str(value)} {obj.curve.tip['unit']}")

def main():
    app = QApplication(sys.argv)
    theprogram = engine()
    theprogram.ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
