from PySide6.QtWidgets import QVBoxLayout, QPushButton, QComboBox, QSlider, QDialog
from PySide6.QtCore import Qt
import pyqtgraph as pg

class PopupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Segment generation mode")

        layout = QVBoxLayout(self)

        # Pyqtgraph plot
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)

        # Button
        self.button2 = QPushButton("OK")
        self.button2.clicked.connect(self.on_button2_clicked)
        layout.addWidget(self.button2)

    def on_button2_clicked(self):
        #selected_value = self.combo_box.currentText()
        self.accept()
        return True #selected_value
