import sys
from PySide6.QtWidgets import QTreeView
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pyqtgraph as pg


class MVexperiment(QStandardItemModel):
    def __init__(self,root):
        super().__init__(self)
        self.createTree()

    def createTree():
         
        

model = QStandardItemModel()
        for row in range(3):
            newrow = QStandardItem(f'Row{row}')            
            model.appendRow(newrow)
            for column in range(2):
                item = QStandardItem(f"row {row}, column {column}")
                newrow.appendRow(item)