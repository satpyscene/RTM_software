# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(861, 557)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionSaveImage = QAction(MainWindow)
        self.actionSaveImage.setObjectName(u"actionSaveImage")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.action_parameter = QAction(MainWindow)
        self.action_parameter.setObjectName(u"action_parameter")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainWidget = QWidget(self.centralwidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 831, 501))
        self.gridLayoutWidget_3 = QWidget(self.mainWidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 821, 491))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressBar = QProgressBar(self.gridLayoutWidget_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setStyleSheet(u"QProgressBar {border: none;text-align: center;}")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.graphicsView = QGraphicsView(self.gridLayoutWidget_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(521, 321))
        self.graphicsView.setMaximumSize(QSize(521, 321))

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(13)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_start = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(0, 40))
        self.pushButton_start.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 127);}")

        self.horizontalLayout_2.addWidget(self.pushButton_start)

        self.pushButton_picset = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_picset.setObjectName(u"pushButton_picset")
        self.pushButton_picset.setMinimumSize(QSize(0, 40))
        self.pushButton_picset.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 127);}")

        self.horizontalLayout_2.addWidget(self.pushButton_picset)

        self.pushButton_draw = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_draw.setObjectName(u"pushButton_draw")
        self.pushButton_draw.setMinimumSize(QSize(0, 40))
        self.pushButton_draw.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 127);}")

        self.horizontalLayout_2.addWidget(self.pushButton_draw)

        self.pushButton_picout = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_picout.setObjectName(u"pushButton_picout")
        self.pushButton_picout.setMinimumSize(QSize(0, 40))
        self.pushButton_picout.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 127);}")

        self.horizontalLayout_2.addWidget(self.pushButton_picout)

        self.pushButton_dataout = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_dataout.setObjectName(u"pushButton_dataout")
        self.pushButton_dataout.setMinimumSize(QSize(0, 40))
        self.pushButton_dataout.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 127);}")

        self.horizontalLayout_2.addWidget(self.pushButton_dataout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 4, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(31, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_atm = QPushButton(self.frame)
        self.pushButton_atm.setObjectName(u"pushButton_atm")
        self.pushButton_atm.setGeometry(QRect(0, 40, 31, 31))
        self.pushButton_cloud = QPushButton(self.frame)
        self.pushButton_cloud.setObjectName(u"pushButton_cloud")
        self.pushButton_cloud.setGeometry(QRect(0, 70, 31, 31))
        self.pushButton_geo = QPushButton(self.frame)
        self.pushButton_geo.setObjectName(u"pushButton_geo")
        self.pushButton_geo.setGeometry(QRect(0, 100, 31, 31))
        self.pushButton_surface = QPushButton(self.frame)
        self.pushButton_surface.setObjectName(u"pushButton_surface")
        self.pushButton_surface.setGeometry(QRect(0, 130, 31, 31))
        self.pushButton_spectral = QPushButton(self.frame)
        self.pushButton_spectral.setObjectName(u"pushButton_spectral")
        self.pushButton_spectral.setGeometry(QRect(0, 160, 31, 31))
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(0, 190, 31, 31))
        self.pushButton_14 = QPushButton(self.frame)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(0, 460, 31, 31))
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(0, 0, 31, 31))

        self.gridLayout_2.addWidget(self.frame, 0, 0, 2, 1)

        self.textEdit_output = QTextEdit(self.gridLayoutWidget_3)
        self.textEdit_output.setObjectName(u"textEdit_output")
        self.textEdit_output.setMaximumSize(QSize(16777215, 80))

        self.gridLayout_2.addWidget(self.textEdit_output, 1, 1, 1, 4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_11)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_10)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.gridLayoutWidget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_11 = QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_11)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 25))

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.pushButton_12, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.line = QFrame(self.gridLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_x1 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_x1.setObjectName(u"lineEdit_x1")
        self.lineEdit_x1.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_x1, 3, 2, 1, 1)

        self.comboBox_colortype = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_colortype.setObjectName(u"comboBox_colortype")
        self.comboBox_colortype.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.comboBox_colortype, 1, 5, 1, 2)

        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 6)

        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)

        self.lineEdit_dpi = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_dpi.setObjectName(u"lineEdit_dpi")
        self.lineEdit_dpi.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_dpi, 4, 2, 1, 2)

        self.label_9 = QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 4, 1, 1)

        self.comboBox_linetype = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_linetype.setObjectName(u"comboBox_linetype")
        self.comboBox_linetype.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.comboBox_linetype, 1, 2, 1, 2)

        self.lineEdit_y2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_y2.setObjectName(u"lineEdit_y2")
        self.lineEdit_y2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_y2, 3, 6, 1, 1)

        self.lineEdit_y1 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_y1.setObjectName(u"lineEdit_y1")
        self.lineEdit_y1.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_y1, 3, 5, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.lineEdit_x2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_x2.setObjectName(u"lineEdit_x2")
        self.lineEdit_x2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_x2, 3, 3, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line_3 = QFrame(self.gridLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(6)
        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.label_15, 3, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 25))
        self.pushButton_13.setMaximumSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.pushButton_13, 3, 3, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.label_14, 2, 2, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 25))
        self.comboBox_2.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_5.addWidget(self.comboBox_2, 2, 3, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))
        self.comboBox.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_5.addWidget(self.comboBox, 2, 1, 1, 1)

        self.putoutpath_lineEdit = QLineEdit(self.gridLayoutWidget_3)
        self.putoutpath_lineEdit.setObjectName(u"putoutpath_lineEdit")
        self.putoutpath_lineEdit.setMinimumSize(QSize(0, 25))
        self.putoutpath_lineEdit.setMaximumSize(QSize(140, 25))

        self.gridLayout_5.addWidget(self.putoutpath_lineEdit, 3, 1, 1, 2)

        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_5)

        self.line_4 = QFrame(self.gridLayoutWidget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.textEdit = QTextEdit(self.gridLayoutWidget_3)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(290, 45))

        self.verticalLayout.addWidget(self.textEdit)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_2.setColumnStretch(2, 5)
        self.pushButton_kill = QPushButton(self.mainWidget)
        self.pushButton_kill.setObjectName(u"pushButton_kill")
        self.pushButton_kill.setGeometry(QRect(830, 60, 41, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 861, 23))
        self.menubar.setDefaultUp(True)
        self.menubar.setNativeMenuBar(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        icon = QIcon()
        icon.addFile(u"../../.designer/\u8f6f\u4ef6\u6d41\u7a0b\u56fe.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_5.setIcon(icon)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionsave)
        self.menu.addAction(self.actionSaveImage)
        self.menu.addSeparator()
        self.menu.addAction(self.actionexit)
        self.menu_4.addAction(self.action_parameter)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.actionSaveImage.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.action_parameter.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.pushButton_picset.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u8bbe\u7f6e", None))
        self.pushButton_draw.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236", None))
        self.pushButton_picout.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bfc\u51fa", None))
        self.pushButton_dataout.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5bfc\u51fa", None))
        self.pushButton_atm.setText(QCoreApplication.translate("MainWindow", u"\u6c14", None))
        self.pushButton_cloud.setText(QCoreApplication.translate("MainWindow", u"\u4e91", None))
        self.pushButton_geo.setText(QCoreApplication.translate("MainWindow", u"\u89c6", None))
        self.pushButton_surface.setText(QCoreApplication.translate("MainWindow", u"\u5730", None))
        self.pushButton_spectral.setText(QCoreApplication.translate("MainWindow", u"\u5149", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u51fa", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u8bbe", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u4e09", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8d44\u6599\u5bfc\u5165", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"/home/bubble/\u684c\u9762/RTSW/GAS_OD_PROFILE_0001", None))
        self.pushButton_12.setText("")
        self.lineEdit_x1.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u56fe\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u989c\u8272", None))
        self.lineEdit_dpi.setText(QCoreApplication.translate("MainWindow", u"600", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"y\u8303\u56f4", None))
        self.lineEdit_y2.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.lineEdit_y1.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DPI", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"x\u8303\u56f4", None))
        self.lineEdit_x2.setText(QCoreApplication.translate("MainWindow", u"600", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7ebf\u578b", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7c7b\u578b", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8def\u5f84", None))
        self.pushButton_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u683c\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u".csv", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u".txt", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))

        self.putoutpath_lineEdit.setText(QCoreApplication.translate("MainWindow", u"/home/bubble/\u684c\u9762/data.csv", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4ea7\u54c1\u5bfc\u51fa", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">\u5927\u6c14\u8f90\u5c04\u4f20\u8f93\u8f6f\u4ef6\u6d4b\u8bd5\u7248</span>(1.1.1.240425_alpha)</p></body></html>", None))
        self.pushButton_kill.setText(QCoreApplication.translate("MainWindow", u"KILL", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
    # retranslateUi

