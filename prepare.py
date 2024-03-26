import sys,os
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog 
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QDir, QModelIndex, QItemSelectionModel
from engine.mainwindow import UI
from engine.popup import PopupWindow
import pyqtgraph as pg
from engine.experiment import MVexperiment
from pathlib import Path

class engine(object):
    def __init__(self) -> None:
        self.ui = UI()
        self.ui.openfile.clicked.connect(self.open_files)
        self.ui.openfolder.clicked.connect(self.open_folder)
        self.model = MVexperiment()
        self.ui.filelist.setModel(self.model)
        self.model.rowsInserted.connect(self.setCurve)
        self.resizeView()
        self.ui.filelist.expanded.connect(self.resizeView)
        
        #self.ui.filelist.selectionModel().currentRowChanged.connect(self.highlight)
        self.ui.filelist.selectionModel().selectionChanged.connect(self.highlight)
        #self.ui.filelist.clicked.connect(self.highlight)
        
    def highlight(self,new,old):
        if old.isEmpty() is False:
            oldnum = old.first().indexes()[0].row()
            rowold = self.model.item(oldnum,0)
            rowold.line.setPen('b')
        newnum = new.first().indexes()[0].row()
        rownew = self.model.item(newnum,0)
        rownew.line.setPen('g')

    def lineclick(self,line):
        self.ui.filelist.selectionModel().select(line.parentitem.index(),QItemSelectionModel.SelectionFlag.SelectCurrent )
        
    def setCurve(self,parent,first,last):
        row = self.model.itemFromIndex(self.model.index(first,0))
        x,y = row.curve.segments[1].getCurve()
        row.line= pg.PlotCurveItem(x,y,pen='b')
        row.line.setClickable(True)
        self.ui.graphleft.addItem(row.line)
        row.line.parentitem = row
        row.line.sigClicked.connect(self.lineclick)
        
    def open_folder(self):
        fname = QFileDialog.getExistingDirectory(self.ui, 'Select the root dir', self.ui.wdir.text() )
        if fname == '' or fname is None or fname[0] == '':
            return
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        self.ui.wdir.setText(fname)
        self.model.createTree(fname)
        self.resizeView()
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)

    def resizeView(self):
        self.ui.filelist.resizeColumnToContents(0)

    def open_files(self):
        filename = QFileDialog.getOpenFileNames(self.ui, 'Select the file', self.ui.wdir.text())
        if filename == '' or filename is None or filename[0] == '' or len(filename[0])==0:
            return
        for fname in filename[0]:
            fname = Path(fname)
            self.model.attach(fname)
            self.ui.wdir.setText(str(fname.parents[0]))
            self.resizeView()
            #popup = PopupWindow(self.ui)
            #if popup.exec() == QDialog.DialogCode.Accepted:
            #    selected_value = popup.on_button2_clicked()
            #    print(selected_value)    

def main():
    app = QApplication(sys.argv)
    theprogram = engine()
    theprogram.ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
