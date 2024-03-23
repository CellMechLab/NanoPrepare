from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QComboBox, QSlider, QDialog
from PyQt6.QtCore import Qt
import pyqtgraph as pg

class PopupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Segment generation mode")

        layout = QVBoxLayout(self)

        # Pyqtgraph plot
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)

        # Combo box
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(self.combo_box)

        # Slider
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Vertical)  # Vertical slider
        layout.addWidget(self.slider)

        # Button
        self.button2 = QPushButton("Button 2")
        self.button2.clicked.connect(self.on_button2_clicked)
        layout.addWidget(self.button2)

    def on_button2_clicked(self):
        selected_value = self.combo_box.currentText()
        self.accept()
        return selected_value
