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

    def open_folder(self):
        fname = QFileDialog.getExistingDirectory(self.ui, 'Select the root dir', './')
        if fname == '' or fname is None or fname[0] == '':
            return

        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        self.ui.wdir.setText(fname)

        self.model = MVexperiment(fname)
        self.ui.filelist.setModel(self.model)

        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)

        

    def open_file(self):
        popup = PopupWindow(self.ui)
        if popup.exec() == QDialog.DialogCode.Accepted:
            selected_value = popup.on_button2_clicked()
            print(selected_value)
    

def main():
    app = QApplication(sys.argv)
    theprogram = engine()
    theprogram.ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
