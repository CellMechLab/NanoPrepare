from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QHBoxLayout, QDialog, QDoubleSpinBox
from PySide6.QtCore import Qt

class PopupWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Segment generation mode")

        layout = QVBoxLayout(self)

        sub2_widget = QWidget()
        sub2_layout = QHBoxLayout(sub2_widget)
        sub2_layout.addWidget(QLabel("Geometry: "))
        self.geometry = QComboBox()
        self.geometry.addItems(["Sphere", "Cylinder", "Cone", "Pyramid"])
        self.geometry.currentTextChanged.connect(self.update_labels)
        sub2_layout.addWidget(self.geometry)
        layout.addWidget(sub2_widget)
        
        sub1_widget = QWidget()
        sub1_layout = QHBoxLayout(sub1_widget)
        self.parameter=QLabel("Radius: ")
        sub1_layout.addWidget(self.parameter)
        self.value = QDoubleSpinBox()
        self.value.setDecimals(3)  # Set the number of decimal places
        self.value.setRange(0.000, 10000.000)
        sub1_layout.addWidget(self.value)
        self.units=QLabel("um")
        sub1_layout.addWidget(self.units)
        layout.addWidget(sub1_widget)
        
        sub3_widget = QWidget()
        sub3_layout = QHBoxLayout(sub3_widget)
        button1 = QPushButton("OK")
        button1.clicked.connect(self.on_ok_clicked)
        button2 = QPushButton("Cancel")
        button2.clicked.connect(self.on_cancel_clicked)
        sub3_layout.addWidget(button1)
        sub3_layout.addWidget(button2)
        layout.addWidget(sub3_widget)

    def update_labels(self):
        geometry = self.geometry.currentText().lower()
        if geometry == 'sphere' or geometry == 'cylinder':
            self.parameter.setText("Radius:")
            self.units.setText("um")
        elif geometry == 'cone' or geometry == 'pyramid':
            self.parameter.setText("Angle:")
            self.units.setText("deg")

    def on_ok_clicked(self):
        self.accept()
        return self.geometry.currentText().lower(),self.value.value()
    def on_cancel_clicked(self):
        self.reject()
        return False