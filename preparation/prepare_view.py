# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prepare.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_radius(object):
    def setupUi(self, radius):
        radius.setObjectName("radius")
        radius.resize(1018, 782)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/backup/ico.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        radius.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(radius)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.c_open = QtWidgets.QComboBox(self.centralwidget)
        self.c_open.setObjectName("c_open")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.horizontalLayout_3.addWidget(self.c_open)
        self.open_selectfolder = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.open_selectfolder.setFont(font)
        self.open_selectfolder.setObjectName("open_selectfolder")
        self.horizontalLayout_3.addWidget(self.open_selectfolder)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.horizontalLayout_3.addWidget(self.save)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mainlist = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainlist.sizePolicy().hasHeightForWidth())
        self.mainlist.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mainlist.setFont(font)
        self.mainlist.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainlist.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mainlist.setLineWidth(0)
        self.mainlist.setMidLineWidth(0)
        self.mainlist.setAnimated(False)
        self.mainlist.setObjectName("mainlist")
        self.horizontalLayout_4.addWidget(self.mainlist)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.g_fdistance = PlotWidget(self.centralwidget)
        self.g_fdistance.setObjectName("g_fdistance")
        self.verticalLayout_6.addWidget(self.g_fdistance)
        self.g_single = PlotWidget(self.centralwidget)
        self.g_single.setObjectName("g_single")
        self.verticalLayout_6.addWidget(self.g_single)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Crop = QtWidgets.QGroupBox(self.centralwidget)
        self.Crop.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Crop.sizePolicy().hasHeightForWidth())
        self.Crop.setSizePolicy(sizePolicy)
        self.Crop.setObjectName("Crop")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Crop)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.crop = QtWidgets.QPushButton(self.Crop)
        self.crop.setObjectName("crop")
        self.verticalLayout_2.addWidget(self.crop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.crop_right = QtWidgets.QCheckBox(self.Crop)
        self.crop_right.setChecked(True)
        self.crop_right.setObjectName("crop_right")
        self.horizontalLayout.addWidget(self.crop_right)
        self.crop_left = QtWidgets.QCheckBox(self.Crop)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crop_left.sizePolicy().hasHeightForWidth())
        self.crop_left.setSizePolicy(sizePolicy)
        self.crop_left.setObjectName("crop_left")
        self.horizontalLayout.addWidget(self.crop_left)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.Crop)
        self.Cantilever = QtWidgets.QGroupBox(self.centralwidget)
        self.Cantilever.setObjectName("Cantilever")
        self.formLayout_2 = QtWidgets.QFormLayout(self.Cantilever)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.Cantilever)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.springconstant = QtWidgets.QDoubleSpinBox(self.Cantilever)
        self.springconstant.setEnabled(False)
        self.springconstant.setDecimals(4)
        self.springconstant.setMaximum(999.99)
        self.springconstant.setProperty("value", 1.0)
        self.springconstant.setObjectName("springconstant")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.springconstant)
        self.label_3 = QtWidgets.QLabel(self.Cantilever)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.geometry = QtWidgets.QComboBox(self.Cantilever)
        self.geometry.setEnabled(False)
        self.geometry.setObjectName("geometry")
        self.geometry.addItem("")
        self.geometry.addItem("")
        self.geometry.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.geometry)
        self.label = QtWidgets.QLabel(self.Cantilever)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tipradius = QtWidgets.QSpinBox(self.Cantilever)
        self.tipradius.setMaximum(999999)
        self.tipradius.setObjectName("tipradius")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tipradius)
        self.verticalLayout_4.addWidget(self.Cantilever)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.curve_segment = QtWidgets.QSpinBox(self.groupBox)
        self.curve_segment.setMaximum(9)
        self.curve_segment.setProperty("value", 1)
        self.curve_segment.setObjectName("curve_segment")
        self.verticalLayout_3.addWidget(self.curve_segment)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.slid_alpha = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slid_alpha.sizePolicy().hasHeightForWidth())
        self.slid_alpha.setSizePolicy(sizePolicy)
        self.slid_alpha.setMaximum(255)
        self.slid_alpha.setSingleStep(1)
        self.slid_alpha.setProperty("value", 100)
        self.slid_alpha.setOrientation(QtCore.Qt.Vertical)
        self.slid_alpha.setObjectName("slid_alpha")
        self.horizontalLayout_2.addWidget(self.slid_alpha)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.cScreen = QtWidgets.QComboBox(self.groupBox_3)
        self.cScreen.setObjectName("cScreen")
        self.cScreen.addItem("")
        self.verticalLayout_8.addWidget(self.cScreen)
        self.tabScreen = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabScreen.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabScreen.setTabsClosable(True)
        self.tabScreen.setObjectName("tabScreen")
        self.verticalLayout_8.addWidget(self.tabScreen)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toggle_activated = QtWidgets.QRadioButton(self.groupBox_2)
        self.toggle_activated.setObjectName("toggle_activated")
        self.verticalLayout.addWidget(self.toggle_activated)
        self.toggle_excluded = QtWidgets.QRadioButton(self.groupBox_2)
        self.toggle_excluded.setStyleSheet("color: red;")
        self.toggle_excluded.setChecked(True)
        self.toggle_excluded.setObjectName("toggle_excluded")
        self.verticalLayout.addWidget(self.toggle_excluded)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayout_7.addWidget(self.splitter_2)
        radius.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(radius)
        self.statusbar.setObjectName("statusbar")
        radius.setStatusBar(self.statusbar)

        self.retranslateUi(radius)
        QtCore.QMetaObject.connectSlotsByName(radius)

    def retranslateUi(self, radius):
        _translate = QtCore.QCoreApplication.translate
        radius.setWindowTitle(_translate("radius", "Nano2021"))
        self.c_open.setItemText(0, _translate("radius", "Optics11"))
        self.c_open.setItemText(1, _translate("radius", "jpk-force"))
        self.c_open.setItemText(2, _translate("radius", "Optics11 2019"))
        self.c_open.setItemText(2, _translate("radius", "Optics11 OLD"))
        self.c_open.setItemText(3, _translate("radius", "Nanosurf export"))
        self.c_open.setItemText(4, _translate("radius", "Easy TSV"))
        self.open_selectfolder.setText(_translate("radius", "Load Folder"))
        self.open_selectfolder.setShortcut(_translate("radius", "Ctrl+S"))
        self.save.setText(_translate("radius", "Save JSON"))
        self.save.setShortcut(_translate("radius", "Ctrl+S"))
        self.mainlist.setSortingEnabled(False)
        self.mainlist.headerItem().setText(0, _translate("radius", "Files"))
        self.Crop.setTitle(_translate("radius", "Crop"))
        self.crop.setText(_translate("radius", "crop 50nm"))
        self.crop_right.setText(_translate("radius", "R"))
        self.crop_left.setText(_translate("radius", "L"))
        self.Cantilever.setTitle(_translate("radius", "Cantilever"))
        self.label_2.setText(_translate("radius", "Spring constant [N/m]"))
        self.label_3.setText(_translate("radius", "Tip geometry"))
        self.geometry.setItemText(0, _translate("radius", "-- select --"))
        self.geometry.setItemText(1, _translate("radius", "Sphere"))
        self.geometry.setItemText(2, _translate("radius", "Cylinder"))
        self.label.setText(_translate("radius", "Tip Radius [nm]"))
        self.groupBox.setTitle(_translate("radius", "Segment"))
        self.groupBox_3.setTitle(_translate("radius", "Screening"))
        self.cScreen.setItemText(0, _translate("radius", "-- select --"))
        self.groupBox_2.setTitle(_translate("radius", "Manual Toggle"))
        self.toggle_activated.setText(_translate("radius", "IN"))
        self.toggle_excluded.setText(_translate("radius", "OUT"))
from pyqtgraph import PlotWidget
