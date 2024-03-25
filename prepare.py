import sys,os
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog 
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QDir
from engine.mainwindow import UI
from engine.popup import PopupWindow
from engine.experiment import MVexperiment

class engine(object):
    def __init__(self) -> None:
        self.ui = UI()
        self.ui.openfile.clicked.connect(self.open_file)
        self.ui.openfolder.clicked.connect(self.open_folder)
        self.model = MVexperiment()
        self.ui.filelist.setModel(self.model)
        self.ui.filelist.resizeColumnToContents(0)
        self.ui.filelist.expanded.connect(self.resizeView)

    def open_folder(self):
        fname = QFileDialog.getExistingDirectory(self.ui, 'Select the root dir', self.ui.wdir)
        if fname == '' or fname is None or fname[0] == '':
            return
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        self.ui.wdir.setText(fname)
        self.model.createTree(fname)
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)

    def resizeView(self):
        self.ui.filelist.resizeColumnToContents(0)

    def open_file(self,filename=None):
        if filename is None:
            filename = QFileDialog.getOpenFileName(self.ui, 'Select the file', self.ui.wdir)
            if filename == '' or filename is None or filename[0] == '':
                return
        self.model.attach(filename)
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
