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
        self.options = QComboBox()
        self.options.addItem('Safe mode')
        self.options.addItem('Euristic mode')
        #self.options.addItem('Shift mode')
        self.options.currentTextChanged.connect(self.reload)
        commands.addWidget(self.options)
        commands.addItem(QSpacerItem(20, 20,  QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        button2 = QPushButton("OK")
        button2.clicked.connect(self.on_button2_clicked)
        button3 = QPushButton("Cancel")
        button3.clicked.connect(self.on_button3_clicked)
        commands.addWidget(button2)
        commands.addWidget(button3)
        
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
        modes = {'Safe mode':'safe','Euristic mode':'euristic','Shift mode':'shift'}
        import openers.chiaro
        for obj in self.haystack:
            obj.curve.segments=[]
            nodi = openers.chiaro.getNodes(obj.curve,mode=modes[self.options.currentText()])
            for i in range(len(nodi) - 1):
                if (nodi[i+1]-nodi[i])<2:
                    continue
                obj.curve.attach(obj.curve.data[nodi[i]:nodi[i + 1],:])
            colors = ['y','c']
            i=0
            for segment in obj.curve.segments:
                x,y = segment.getCurve('FT')
                line = self.plot_widget.plot(x,y,pen=colors[i%2])
                line.setAlpha(0.4, False)
                i+=1    
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)         

    def on_button2_clicked(self):
        self.accept()
        return True

    def on_button3_clicked(self):
        self.reject()
        return False