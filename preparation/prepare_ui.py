# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prepare.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QSplitter, QStatusBar,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_radius(object):
    def setupUi(self, radius):
        if not radius.objectName():
            radius.setObjectName(u"radius")
        radius.resize(1018, 726)
        icon = QIcon()
        icon.addFile(u"../../.designer/backup/ico.svg", QSize(), QIcon.Normal, QIcon.Off)
        radius.setWindowIcon(icon)
        self.centralwidget = QWidget(radius)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.c_open = QComboBox(self.centralwidget)
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.addItem("")
        self.c_open.setObjectName(u"c_open")

        self.horizontalLayout_3.addWidget(self.c_open)

        self.open_selectfolder = QPushButton(self.centralwidget)
        self.open_selectfolder.setObjectName(u"open_selectfolder")
        font = QFont()
        font.setBold(True)
        self.open_selectfolder.setFont(font)

        self.horizontalLayout_3.addWidget(self.open_selectfolder)

        self.save = QPushButton(self.centralwidget)
        self.save.setObjectName(u"save")
        self.save.setFont(font)

        self.horizontalLayout_3.addWidget(self.save)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.mainlist = QTreeWidget(self.centralwidget)
        self.mainlist.setObjectName(u"mainlist")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainlist.sizePolicy().hasHeightForWidth())
        self.mainlist.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.mainlist.setFont(font1)
        self.mainlist.setFrameShape(QFrame.StyledPanel)
        self.mainlist.setFrameShadow(QFrame.Sunken)
        self.mainlist.setLineWidth(0)
        self.mainlist.setMidLineWidth(0)
        self.mainlist.setSortingEnabled(False)
        self.mainlist.setAnimated(False)

        self.horizontalLayout_4.addWidget(self.mainlist)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.g_fdistance = PlotWidget(self.centralwidget)
        self.g_fdistance.setObjectName(u"g_fdistance")

        self.verticalLayout_6.addWidget(self.g_fdistance)

        self.g_single = PlotWidget(self.centralwidget)
        self.g_single.setObjectName(u"g_single")

        self.verticalLayout_6.addWidget(self.g_single)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Crop = QGroupBox(self.centralwidget)
        self.Crop.setObjectName(u"Crop")
        self.Crop.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Crop.sizePolicy().hasHeightForWidth())
        self.Crop.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.Crop)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.crop = QPushButton(self.Crop)
        self.crop.setObjectName(u"crop")

        self.verticalLayout_2.addWidget(self.crop)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.crop_right = QCheckBox(self.Crop)
        self.crop_right.setObjectName(u"crop_right")
        self.crop_right.setChecked(True)

        self.horizontalLayout.addWidget(self.crop_right)

        self.crop_left = QCheckBox(self.Crop)
        self.crop_left.setObjectName(u"crop_left")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.crop_left.sizePolicy().hasHeightForWidth())
        self.crop_left.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.crop_left)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.Crop)

        self.Cantilever = QGroupBox(self.centralwidget)
        self.Cantilever.setObjectName(u"Cantilever")
        self.formLayout_2 = QFormLayout(self.Cantilever)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.Cantilever)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.springconstant = QDoubleSpinBox(self.Cantilever)
        self.springconstant.setObjectName(u"springconstant")
        self.springconstant.setEnabled(False)
        self.springconstant.setDecimals(4)
        self.springconstant.setMaximum(999.990000000000009)
        self.springconstant.setValue(1.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.springconstant)

        self.label_3 = QLabel(self.Cantilever)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.geometry = QComboBox(self.Cantilever)
        self.geometry.addItem("")
        self.geometry.addItem("")
        self.geometry.addItem("")
        self.geometry.addItem("")
        self.geometry.addItem("")
        self.geometry.addItem("")
        self.geometry.setObjectName(u"geometry")
        self.geometry.setEnabled(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.geometry)

        self.geometry_label = QLabel(self.Cantilever)
        self.geometry_label.setObjectName(u"geometry_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.geometry_label)

        self.tipradius = QSpinBox(self.Cantilever)
        self.tipradius.setObjectName(u"tipradius")
        self.tipradius.setMaximum(999999)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.tipradius)


        self.verticalLayout_4.addWidget(self.Cantilever)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.curve_segment = QSpinBox(self.groupBox)
        self.curve_segment.setObjectName(u"curve_segment")
        self.curve_segment.setMaximum(9)
        self.curve_segment.setValue(1)

        self.verticalLayout_3.addWidget(self.curve_segment)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.slid_alpha = QSlider(self.centralwidget)
        self.slid_alpha.setObjectName(u"slid_alpha")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.slid_alpha.sizePolicy().hasHeightForWidth())
        self.slid_alpha.setSizePolicy(sizePolicy3)
        self.slid_alpha.setMaximum(255)
        self.slid_alpha.setSingleStep(1)
        self.slid_alpha.setValue(100)
        self.slid_alpha.setOrientation(Qt.Vertical)

        self.horizontalLayout_2.addWidget(self.slid_alpha)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.cScreen = QComboBox(self.groupBox_3)
        self.cScreen.addItem("")
        self.cScreen.setObjectName(u"cScreen")

        self.verticalLayout_8.addWidget(self.cScreen)

        self.tabScreen = QTabWidget(self.groupBox_3)
        self.tabScreen.setObjectName(u"tabScreen")
        self.tabScreen.setTabPosition(QTabWidget.West)
        self.tabScreen.setTabsClosable(True)

        self.verticalLayout_8.addWidget(self.tabScreen)


        self.verticalLayout_5.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.toggle_activated = QRadioButton(self.groupBox_2)
        self.toggle_activated.setObjectName(u"toggle_activated")

        self.verticalLayout.addWidget(self.toggle_activated)

        self.toggle_excluded = QRadioButton(self.groupBox_2)
        self.toggle_excluded.setObjectName(u"toggle_excluded")
        self.toggle_excluded.setStyleSheet(u"color: red;")
        self.toggle_excluded.setChecked(True)

        self.verticalLayout.addWidget(self.toggle_excluded)


        self.verticalLayout_5.addWidget(self.groupBox_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter_2.addWidget(self.splitter)

        self.verticalLayout_7.addWidget(self.splitter_2)

        radius.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(radius)
        self.statusbar.setObjectName(u"statusbar")
        radius.setStatusBar(self.statusbar)

        self.retranslateUi(radius)

        QMetaObject.connectSlotsByName(radius)
    # setupUi

    def retranslateUi(self, radius):
        radius.setWindowTitle(QCoreApplication.translate("radius", u"Nano2021", None))
        self.c_open.setItemText(0, QCoreApplication.translate("radius", u"Optics11", None))
        self.c_open.setItemText(1, QCoreApplication.translate("radius", u"jpk-fmap", None))
        self.c_open.setItemText(2, QCoreApplication.translate("radius", u"jpk-force", None))
        self.c_open.setItemText(3, QCoreApplication.translate("radius", u"Optics11 2019", None))
        self.c_open.setItemText(4, QCoreApplication.translate("radius", u"Optics11 OLD", None))
        self.c_open.setItemText(5, QCoreApplication.translate("radius", u"Nanosurf export", None))
        self.c_open.setItemText(6, QCoreApplication.translate("radius", u"Easy TSV", None))

        self.open_selectfolder.setText(QCoreApplication.translate("radius", u"Load Folder", None))
#if QT_CONFIG(shortcut)
        self.open_selectfolder.setShortcut(QCoreApplication.translate("radius", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.save.setText(QCoreApplication.translate("radius", u"Save JSON", None))
#if QT_CONFIG(shortcut)
        self.save.setShortcut(QCoreApplication.translate("radius", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        ___qtreewidgetitem = self.mainlist.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("radius", u"Files", None));
        self.Crop.setTitle(QCoreApplication.translate("radius", u"Crop", None))
        self.crop.setText(QCoreApplication.translate("radius", u"crop 50nm", None))
        self.crop_right.setText(QCoreApplication.translate("radius", u"R", None))
        self.crop_left.setText(QCoreApplication.translate("radius", u"L", None))
        self.Cantilever.setTitle(QCoreApplication.translate("radius", u"Cantilever", None))
        self.label_2.setText(QCoreApplication.translate("radius", u"Spring constant [N/m]", None))
        self.label_3.setText(QCoreApplication.translate("radius", u"Tip geometry", None))
        self.geometry.setItemText(0, QCoreApplication.translate("radius", u"-- select --", None))
        self.geometry.setItemText(1, QCoreApplication.translate("radius", u"Sphere", None))
        self.geometry.setItemText(2, QCoreApplication.translate("radius", u"Cylinder", None))
        self.geometry.setItemText(3, QCoreApplication.translate("radius", u"Cone", None))
        self.geometry.setItemText(4, QCoreApplication.translate("radius", u"Pyramid", None))
        self.geometry.setItemText(5, QCoreApplication.translate("radius", u"Other", None))

        self.geometry_label.setText(QCoreApplication.translate("radius", u"Tip Radius [nm]", None))
        self.groupBox.setTitle(QCoreApplication.translate("radius", u"Segment", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("radius", u"Screening", None))
        self.cScreen.setItemText(0, QCoreApplication.translate("radius", u"-- select --", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("radius", u"Manual Toggle", None))
        self.toggle_activated.setText(QCoreApplication.translate("radius", u"IN", None))
        self.toggle_excluded.setText(QCoreApplication.translate("radius", u"OUT", None))
    # retranslateUi

