from PySide6.QtWidgets import QApplication,QHBoxLayout, QVBoxLayout, QPushButton, QComboBox, QSpacerItem, QDialog, QSizePolicy
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

        commands = QHBoxLayout()
        options = QComboBox()
        options.addItem('Safe mode')
        options.addItem('Euristic mode')
        options.addItem('Shift mode')
        options.currentTextChanged.connect(self.reload)
        commands.addWidget(options)
        commands.addItem(QSpacerItem(20, 20,  QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        button2 = QPushButton("OK")
        button2.clicked.connect(self.on_button2_clicked)
        commands.addWidget(button2)
        
        layout.addLayout(commands)
        
    def prepare(self,haystack):
        self.haystack = haystack
        self.plot_widget.clear()
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        for obj in self.haystack:
            colors = ['y','c']
            i=0
            for segment in obj.curve.segments:
                x,y = segment.getCurve('FT')
                line = self.plot_widget.plot(x,y,pen=colors[i%2])
                line.setAlpha(0.4, False)
                i+=1    
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        
    def reload(self,mode):
        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        
        #recreate segments
        self.plot_widget.clear()
        
        for obj in self.haystack:
            colors = ['y','c']
            i=0
            for segment in obj.curve.segments:
                x,y = segment.getCurve('FT')
                line = self.plot_widget.plot(x,y,pen=colors[i%2])
                line.setAlpha(0.4, False)
                i+=1    
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)         

    def on_button2_clicked(self):
        #selected_value = self.combo_box.currentText()
        self.accept()
        return True #selected_value
