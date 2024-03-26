import sys,os
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog 
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QDir
from engine.mainwindow import UI
from engine.popup import PopupWindow
from engine.experiment import MVexperiment
from pathlib import Path

class engine(object):
    def __init__(self) -> None:
        self.ui = UI()
        self.ui.openfile.clicked.connect(self.open_file)
        self.ui.openfolder.clicked.connect(self.open_folder)
        self.model = MVexperiment()
        self.ui.filelist.setModel(self.model)
        self.model.rowsInserted.connect(self.setCurve)
        self.resizeView()
        self.ui.filelist.expanded.connect(self.resizeView)
        
        self.ui.filelist.selectionModel().currentRowChanged.connect(self.highlight)
        #self.ui.filelist.clicked.connect(self.highlight)
        
    def highlight(self,new,old):
        print(new,old)
        #row = self.model.itemFromIndex(obj)
        #row.line.setPen(color='r')

    def setCurve(self,parent,first,last):
        row = self.model.itemFromIndex(self.model.index(first,0))
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 4, 5, 6]
        row.line = self.ui.graphleft.plot(x, y, pen='b')
        

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

    def open_file(self):
        filename = QFileDialog.getOpenFileName(self.ui, 'Select the file', self.ui.wdir.text())
        if filename == '' or filename is None or filename[0] == '':
            return
        filename = Path(filename[0])
        self.model.attach(filename)
        self.ui.wdir.setText(str(filename.parents[0]))
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
