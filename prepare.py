import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from mainwindow import UI

class engine(object):
    def __init__(self) -> None:
        self.ui = UI()

def main():
    app = QApplication(sys.argv)
    theprogram = engine()
    theprogram.ui.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
