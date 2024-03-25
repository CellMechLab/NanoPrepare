import sys
from PySide6.QtWidgets import QSpacerItem,QTreeView, QMainWindow, QVBoxLayout, QWidget, QPushButton, QComboBox, QHBoxLayout, QSlider, QLabel, QSizePolicy
from PySide6.QtCore import Qt
import pyqtgraph as pg

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window title and geometry
        self.setWindowTitle("O11 Prepare")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Group 1: Button, QComboBox, and List
        group1_layout = QHBoxLayout()
        self.openfile = QPushButton("Open file")
        self.openfolder = QPushButton("Open folder")
        self.nfiles = QLabel("0")
        self.wdir = QLabel("./")
        group1_layout.addWidget(self.openfile)
        group1_layout.addWidget(self.openfolder)
        group1_layout.addWidget(QLabel("Opened files: "))
        group1_layout.addWidget(self.nfiles)
        group1_layout.addWidget(QLabel(" - Working dir: "))
        group1_layout.addWidget(self.wdir)
        spacer = QSpacerItem(20, 20,  QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        group1_layout.addItem( spacer )
        layout.addLayout(group1_layout)

        # Group 2: Horizontal Slider and two PyQtGraph PlotWidgets
        group2_layout = QHBoxLayout()
        slider = QSlider(  )
        slider.setOrientation( Qt.Orientation.Vertical )  # Vertical slider
        plot_widget1 = pg.PlotWidget()
        plot_widget2 = pg.PlotWidget()
        group2_layout.addWidget(slider)
        group2_layout.addWidget(plot_widget1, stretch=1)
        group2_layout.addWidget(plot_widget2, stretch=1)
        layout.addLayout(group2_layout)

        # Group 3: Button and Group of widgets
        group3_layout = QVBoxLayout()
        button2 = QPushButton("Button 2")
        self.filelist = QTreeView()
        group3_layout.addWidget(self.filelist)
        group3_layout.addWidget(button2)
        sub_widget = QWidget()
        sub_layout = QVBoxLayout(sub_widget)
        sub_layout.addWidget(QLabel("Sub Widget 1"))
        sub_layout.addWidget(QLabel("Sub Widget 2"))
        group3_layout.addWidget(sub_widget)
        layout.addLayout(group3_layout)