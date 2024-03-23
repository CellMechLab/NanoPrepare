import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtCore import Qt
from engine.mainwindow import UI
from engine.popup import PopupWindow

class engine(object):
    def __init__(self) -> None:
        self.ui = UI()
        self.ui.openfile.clicked.connect(self.open_file)
        self.ui.openfolder.clicked.connect(self.open_folder)

    def open_folder(self):
        pass

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
