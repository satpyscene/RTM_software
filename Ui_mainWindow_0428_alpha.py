# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow_0428_alpha.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 561)
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
        self.mainWidget.setGeometry(QRect(0, 0, 1091, 511))
        self.gridLayoutWidget_3 = QWidget(self.mainWidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 901, 491))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressBar = QProgressBar(self.gridLayoutWidget_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(521, 0))
        self.progressBar.setMaximumSize(QSize(521, 16777215))
        self.progressBar.setStyleSheet(u"QProgressBar {border: none;text-align: center;\n"
"							}\n"
"QProgressBar::chunk {\n"
"    background-color:  rgba(255, 0, 0, 127);;\n"
"}")
        self.progressBar.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.graphicsView = QGraphicsView(self.gridLayoutWidget_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(521, 321))
        self.graphicsView.setMaximumSize(QSize(521, 321))
        self.graphicsView.setLayoutDirection(Qt.LeftToRight)
        self.graphicsView.setFrameShape(QFrame.StyledPanel)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(13)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_start = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(0, 40))
        self.pushButton_start.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_start)

        self.picset = QPushButton(self.gridLayoutWidget_3)
        self.picset.setObjectName(u"picset")
        self.picset.setMinimumSize(QSize(0, 40))
        self.picset.setStyleSheet(u"QPushButton {background-color: rgba(255, 255, 255, 127);}")

        self.horizontalLayout_2.addWidget(self.picset)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_creatnewcase = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_creatnewcase.setObjectName(u"pushButton_creatnewcase")
        self.pushButton_creatnewcase.setMaximumSize(QSize(60, 16777215))
        self.pushButton_creatnewcase.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.pushButton_creatnewcase)

        self.pushButton_opencase = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_opencase.setObjectName(u"pushButton_opencase")
        self.pushButton_opencase.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_opencase)

        self.pushButton_savecase = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_savecase.setObjectName(u"pushButton_savecase")
        self.pushButton_savecase.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_savecase)

        self.pushButton_casesaveas = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_casesaveas.setObjectName(u"pushButton_casesaveas")
        self.pushButton_casesaveas.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_casesaveas)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.stackedWidget = QStackedWidget(self.gridLayoutWidget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_picset = QWidget()
        self.page_picset.setObjectName(u"page_picset")
        self.layoutWidget = QWidget(self.page_picset)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 321, 151))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_x1 = QLineEdit(self.layoutWidget)
        self.lineEdit_x1.setObjectName(u"lineEdit_x1")
        self.lineEdit_x1.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_x1, 3, 2, 1, 1)

        self.comboBox_colortype = QComboBox(self.layoutWidget)
        self.comboBox_colortype.setObjectName(u"comboBox_colortype")
        self.comboBox_colortype.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.comboBox_colortype, 1, 5, 1, 2)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 6)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)

        self.lineEdit_dpi = QLineEdit(self.layoutWidget)
        self.lineEdit_dpi.setObjectName(u"lineEdit_dpi")
        self.lineEdit_dpi.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_dpi, 4, 2, 1, 2)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 4, 1, 1)

        self.comboBox_linetype = QComboBox(self.layoutWidget)
        self.comboBox_linetype.setObjectName(u"comboBox_linetype")
        self.comboBox_linetype.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.comboBox_linetype, 1, 2, 1, 2)

        self.lineEdit_y2 = QLineEdit(self.layoutWidget)
        self.lineEdit_y2.setObjectName(u"lineEdit_y2")
        self.lineEdit_y2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_y2, 3, 6, 1, 1)

        self.lineEdit_y1 = QLineEdit(self.layoutWidget)
        self.lineEdit_y1.setObjectName(u"lineEdit_y1")
        self.lineEdit_y1.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_y1, 3, 5, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 1, 1, 1)

        self.lineEdit_x2 = QLineEdit(self.layoutWidget)
        self.lineEdit_x2.setObjectName(u"lineEdit_x2")
        self.lineEdit_x2.setMaximumSize(QSize(16777215, 25))

        self.gridLayout.addWidget(self.lineEdit_x2, 3, 3, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_picset)
        self.page_output = QWidget()
        self.page_output.setObjectName(u"page_output")
        self.verticalLayoutWidget = QWidget(self.page_output)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 311, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(60, 0))
        self.label_13.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_16.addWidget(self.label_13)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))
        self.comboBox.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_16.addWidget(self.comboBox)

        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(10000, 20))
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.label_14)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 25))
        self.comboBox_2.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_16.addWidget(self.comboBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(60, 0))
        self.label_15.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_3.addWidget(self.label_15)

        self.putoutpath_lineEdit = QLineEdit(self.verticalLayoutWidget)
        self.putoutpath_lineEdit.setObjectName(u"putoutpath_lineEdit")
        self.putoutpath_lineEdit.setMinimumSize(QSize(0, 25))
        self.putoutpath_lineEdit.setMaximumSize(QSize(100000, 25))

        self.horizontalLayout_3.addWidget(self.putoutpath_lineEdit)

        self.pushButton_13 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(0, 25))
        self.pushButton_13.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_13)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_output)
        self.page_atm = QWidget()
        self.page_atm.setObjectName(u"page_atm")
        self.gridLayoutWidget = QWidget(self.page_atm)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 321, 341))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.label)

        self.atm_comboBox_model = QComboBox(self.gridLayoutWidget)
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.setObjectName(u"atm_comboBox_model")

        self.horizontalLayout_5.addWidget(self.atm_comboBox_model)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(59, 16777215))

        self.horizontalLayout_6.addWidget(self.label_2)

        self.comboBox_profile = QComboBox(self.gridLayoutWidget)
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.addItem("")
        self.comboBox_profile.setObjectName(u"comboBox_profile")
        self.comboBox_profile.setMaximumSize(QSize(195, 16777215))

        self.horizontalLayout_6.addWidget(self.comboBox_profile)

        self.lineview = QPushButton(self.gridLayoutWidget)
        self.lineview.setObjectName(u"lineview")
        self.lineview.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_6.addWidget(self.lineview)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_12.addWidget(self.lineEdit)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_12.addWidget(self.pushButton_12)


        self.gridLayout_4.addLayout(self.horizontalLayout_12, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_atm)
        self.page_cloud = QWidget()
        self.page_cloud.setObjectName(u"page_cloud")
        self.widget = QWidget(self.page_cloud)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 291, 121))
        self.gridLayout_7 = QGridLayout(self.widget)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.comboBox_4 = QComboBox(self.widget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_7.addWidget(self.comboBox_4, 0, 1, 1, 2)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_7.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_7.addWidget(self.label_21, 3, 2, 1, 1)

        self.cloud_lineEdit_width = QLineEdit(self.widget)
        self.cloud_lineEdit_width.setObjectName(u"cloud_lineEdit_width")

        self.gridLayout_7.addWidget(self.cloud_lineEdit_width, 3, 1, 1, 1)

        self.cloud_lineEdit_height = QLineEdit(self.widget)
        self.cloud_lineEdit_height.setObjectName(u"cloud_lineEdit_height")

        self.gridLayout_7.addWidget(self.cloud_lineEdit_height, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 1, 2, 1, 1)

        self.cloud_switch = QCheckBox(self.widget)
        self.cloud_switch.setObjectName(u"cloud_switch")

        self.gridLayout_7.addWidget(self.cloud_switch, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_cloud)
        self.page_geo = QWidget()
        self.page_geo.setObjectName(u"page_geo")
        self.gridLayoutWidget_4 = QWidget(self.page_geo)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 321, 347))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.graphicsView_3 = QGraphicsView(self.gridLayoutWidget_4)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setMinimumSize(QSize(0, 140))

        self.gridLayout_9.addWidget(self.graphicsView_3, 2, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_29 = QLabel(self.gridLayoutWidget_4)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_10.addWidget(self.label_29, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.gridLayoutWidget_4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_10.addWidget(self.checkBox_3, 4, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_10.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_10.addWidget(self.label_28, 2, 0, 1, 1)

        self.line_6 = QFrame(self.gridLayoutWidget_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_10.addWidget(self.line_6, 5, 0, 1, 3)

        self.label_30 = QLabel(self.gridLayoutWidget_4)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_10.addWidget(self.label_30, 3, 0, 1, 1)

        self.detector_slider = QSlider(self.gridLayoutWidget_4)
        self.detector_slider.setObjectName(u"detector_slider")
        self.detector_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.detector_slider, 1, 3, 1, 1)

        self.target_slider = QSlider(self.gridLayoutWidget_4)
        self.target_slider.setObjectName(u"target_slider")
        self.target_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.target_slider, 2, 3, 1, 1)

        self.angle_slider = QSlider(self.gridLayoutWidget_4)
        self.angle_slider.setObjectName(u"angle_slider")
        self.angle_slider.setOrientation(Qt.Horizontal)

        self.gridLayout_10.addWidget(self.angle_slider, 3, 3, 1, 1)

        self.target_input = QLineEdit(self.gridLayoutWidget_4)
        self.target_input.setObjectName(u"target_input")

        self.gridLayout_10.addWidget(self.target_input, 2, 1, 1, 2)

        self.geo_lineEdit_angel = QLineEdit(self.gridLayoutWidget_4)
        self.geo_lineEdit_angel.setObjectName(u"geo_lineEdit_angel")

        self.gridLayout_10.addWidget(self.geo_lineEdit_angel, 3, 1, 1, 2)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_10.addWidget(self.lineEdit_9, 4, 1, 1, 3)

        self.comboBox_7 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_10.addWidget(self.comboBox_7, 0, 1, 1, 3)

        self.detector_input = QLineEdit(self.gridLayoutWidget_4)
        self.detector_input.setObjectName(u"detector_input")

        self.gridLayout_10.addWidget(self.detector_input, 1, 1, 1, 2)


        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_geo)
        self.page_surface = QWidget()
        self.page_surface.setObjectName(u"page_surface")
        self.verticalLayoutWidget_2 = QWidget(self.page_surface)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 321, 341))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_31 = QLabel(self.verticalLayoutWidget_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(60, 0))

        self.gridLayout_11.addWidget(self.label_31, 1, 0, 1, 1)

        self.comboBox_9 = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout_11.addWidget(self.comboBox_9, 1, 2, 1, 3)

        self.label_32 = QLabel(self.verticalLayoutWidget_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(60, 0))

        self.gridLayout_11.addWidget(self.label_32, 2, 0, 1, 1)

        self.surface_lineEdit_TEMP = QLineEdit(self.verticalLayoutWidget_2)
        self.surface_lineEdit_TEMP.setObjectName(u"surface_lineEdit_TEMP")

        self.gridLayout_11.addWidget(self.surface_lineEdit_TEMP, 2, 2, 1, 1)

        self.radioButton = QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout_11.addWidget(self.radioButton, 2, 3, 1, 1)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout_11.addWidget(self.radioButton_2, 2, 4, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_11)

        self.line_7 = QFrame(self.verticalLayoutWidget_2)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_7)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_33 = QLabel(self.verticalLayoutWidget_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_13.addWidget(self.label_33)

        self.surface_lineEdit_reflection = QLineEdit(self.verticalLayoutWidget_2)
        self.surface_lineEdit_reflection.setObjectName(u"surface_lineEdit_reflection")

        self.horizontalLayout_13.addWidget(self.surface_lineEdit_reflection)


        self.gridLayout_12.addLayout(self.horizontalLayout_13, 0, 0, 1, 5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_34 = QLabel(self.verticalLayoutWidget_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_14.addWidget(self.label_34)

        self.comboBox_11 = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.horizontalLayout_14.addWidget(self.comboBox_11)

        self.label_38 = QLabel(self.verticalLayoutWidget_2)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_14.addWidget(self.label_38)

        self.lineEdit_11 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_14.addWidget(self.lineEdit_11)


        self.gridLayout_12.addLayout(self.horizontalLayout_14, 1, 0, 1, 5)

        self.gridLayout_12.setColumnStretch(0, 1)

        self.verticalLayout_5.addLayout(self.gridLayout_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_35 = QLabel(self.verticalLayoutWidget_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_15.addWidget(self.label_35)

        self.comboBox_10 = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.horizontalLayout_15.addWidget(self.comboBox_10)

        self.label_36 = QLabel(self.verticalLayoutWidget_2)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_15.addWidget(self.label_36)

        self.lineEdit_10 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_15.addWidget(self.lineEdit_10)

        self.label_37 = QLabel(self.verticalLayoutWidget_2)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_15.addWidget(self.label_37)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.page_surface)
        self.page_sp = QWidget()
        self.page_sp.setObjectName(u"page_sp")
        self.gridLayoutWidget_5 = QWidget(self.page_sp)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 322, 341))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.comboBox_12 = QComboBox(self.gridLayoutWidget_5)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setMinimumSize(QSize(230, 0))

        self.gridLayout_13.addWidget(self.comboBox_12, 1, 1, 1, 2)

        self.sp_comboBox_resolution = QComboBox(self.gridLayoutWidget_5)
        self.sp_comboBox_resolution.addItem("")
        self.sp_comboBox_resolution.addItem("")
        self.sp_comboBox_resolution.addItem("")
        self.sp_comboBox_resolution.addItem("")
        self.sp_comboBox_resolution.setObjectName(u"sp_comboBox_resolution")

        self.gridLayout_13.addWidget(self.sp_comboBox_resolution, 5, 1, 1, 2)

        self.label_42 = QLabel(self.gridLayoutWidget_5)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_13.addWidget(self.label_42, 5, 0, 1, 1)

        self.sp_lineEdit_wavmax = QLineEdit(self.gridLayoutWidget_5)
        self.sp_lineEdit_wavmax.setObjectName(u"sp_lineEdit_wavmax")
        self.sp_lineEdit_wavmax.setMinimumSize(QSize(80, 0))
        self.sp_lineEdit_wavmax.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_13.addWidget(self.sp_lineEdit_wavmax, 2, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_13.addWidget(self.label_12, 0, 0, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_5)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_13.addWidget(self.label_39, 2, 0, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_5)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_13.addWidget(self.label_41, 6, 0, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_17, 7, 0, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_5)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_13.addWidget(self.label_40, 1, 0, 1, 1)

        self.sp_comboBox_streams = QComboBox(self.gridLayoutWidget_5)
        self.sp_comboBox_streams.addItem("")
        self.sp_comboBox_streams.addItem("")
        self.sp_comboBox_streams.addItem("")
        self.sp_comboBox_streams.addItem("")
        self.sp_comboBox_streams.setObjectName(u"sp_comboBox_streams")

        self.gridLayout_13.addWidget(self.sp_comboBox_streams, 6, 1, 1, 2)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget_5)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_13.addWidget(self.comboBox_3, 0, 1, 1, 2)

        self.sp_lineEdit_wavmin = QLineEdit(self.gridLayoutWidget_5)
        self.sp_lineEdit_wavmin.setObjectName(u"sp_lineEdit_wavmin")
        self.sp_lineEdit_wavmin.setMinimumSize(QSize(80, 0))
        self.sp_lineEdit_wavmin.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_13.addWidget(self.sp_lineEdit_wavmin, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_sp)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.textEdit_output = QTextEdit(self.gridLayoutWidget_3)
        self.textEdit_output.setObjectName(u"textEdit_output")
        self.textEdit_output.setMaximumSize(QSize(16777215, 80))
        self.textEdit_output.setFrameShadow(QFrame.Sunken)
        self.textEdit_output.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_output.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_2.addWidget(self.textEdit_output, 1, 1, 1, 2)

        self.frame_2 = QFrame(self.gridLayoutWidget_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(31, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_19 = QPushButton(self.frame_2)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(0, 460, 31, 31))
        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(0, 0, 31, 31))
        self.atm = QPushButton(self.frame_2)
        self.atm.setObjectName(u"atm")
        self.atm.setGeometry(QRect(0, 40, 31, 31))
        self.cloud = QPushButton(self.frame_2)
        self.cloud.setObjectName(u"cloud")
        self.cloud.setGeometry(QRect(0, 70, 31, 31))
        self.geo = QPushButton(self.frame_2)
        self.geo.setObjectName(u"geo")
        self.geo.setGeometry(QRect(0, 100, 31, 31))
        self.surface = QPushButton(self.frame_2)
        self.surface.setObjectName(u"surface")
        self.surface.setGeometry(QRect(0, 130, 31, 31))
        self.spectral = QPushButton(self.frame_2)
        self.spectral.setObjectName(u"spectral")
        self.spectral.setGeometry(QRect(0, 160, 31, 31))
        self.putout = QPushButton(self.frame_2)
        self.putout.setObjectName(u"putout")
        self.putout.setGeometry(QRect(0, 190, 31, 31))

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 2, 1)

        self.frame = QFrame(self.mainWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(1040, 10, 31, 489))
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
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(-5, -9, 1111, 671))
        MainWindow.setCentralWidget(self.centralwidget)
        self.graphicsView_2.raise_()
        self.mainWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 923, 23))
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

        self.stackedWidget.setCurrentIndex(4)


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
        self.picset.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236\u8bbe\u7f6e", None))
        self.pushButton_draw.setText(QCoreApplication.translate("MainWindow", u"\u7ed8\u5236", None))
        self.pushButton_picout.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u5bfc\u51fa", None))
        self.pushButton_dataout.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5bfc\u51fa", None))
        self.pushButton_creatnewcase.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.pushButton_opencase.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_savecase.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_casesaveas.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
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
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u683c\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u".csv", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u".txt", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8def\u5f84", None))
        self.putoutpath_lineEdit.setText(QCoreApplication.translate("MainWindow", u"/home/bubble/\u684c\u9762/data.csv", None))
        self.pushButton_13.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5927\u6c14\u6a21\u5f0f", None))
        self.atm_comboBox_model.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7528\u6237\u81ea\u5b9a\u4e49", None))
        self.atm_comboBox_model.setItemText(1, QCoreApplication.translate("MainWindow", u"\u70ed\u5e26", None))
        self.atm_comboBox_model.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e2d\u7eac\u5ea6\u590f\u5929", None))
        self.atm_comboBox_model.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e2d\u7eac\u5ea6\u51ac\u5929", None))
        self.atm_comboBox_model.setItemText(4, QCoreApplication.translate("MainWindow", u"\u4e9a\u5317\u6781\u590f\u5929", None))
        self.atm_comboBox_model.setItemText(5, QCoreApplication.translate("MainWindow", u"\u4e9a\u5317\u6781\u51ac\u5929", None))
        self.atm_comboBox_model.setItemText(6, QCoreApplication.translate("MainWindow", u"\u7f8e\u56fd\u6807\u51c6\u5927\u6c14", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5ed3\u7ebf\u7c7b\u578b", None))
        self.comboBox_profile.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6e29\u5ea6", None))
        self.comboBox_profile.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6c34\u6c7d", None))
        self.comboBox_profile.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e8c\u6c27\u5316\u78b3", None))
        self.comboBox_profile.setItemText(3, QCoreApplication.translate("MainWindow", u"\u81ed\u6c27", None))

        self.lineview.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8d44\u6599\u5bfc\u5165", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"/home/bubble/\u684c\u9762/RTSW/GAS_OD_PROFILE_0001", None))
        self.pushButton_12.setText("")
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u51b0\u4e91", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6c34\u4e91", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u9ad8", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u539a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.cloud_lineEdit_width.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cloud_lineEdit_height.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"hpa", None))
        self.cloud_switch.setText(QCoreApplication.translate("MainWindow", u"\u4e91\u6a21\u5f0f", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u51e0\u4f55\u8def\u5f84", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u5730\u7403\u66f2\u7387", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u6d4b\u4f4d\u7f6e", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u7269\u9ad8\u5ea6", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u6d4b/\u76ee\u6807\u5929\u9876\u89d2", None))
        self.target_input.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.geo_lineEdit_angel.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"\u659c\u7a0b", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6c34\u5e73", None))

        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u5730\u8868\u7c7b\u578b", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6052\u5b9a\u53cd\u5c04\u7387", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6717\u4f2f\u4f53", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"BRDF", None))

        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u5730\u8868\u6e29\u5ea6", None))
        self.surface_lineEdit_TEMP.setText(QCoreApplication.translate("MainWindow", u"273", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"^\u3002C", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u5730\u8868\u53cd\u5c04\u7387", None))
        self.surface_lineEdit_reflection.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u6717\u4f2f\u4f53\u7c7b\u578b", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"LOS\u6307\u6570", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"BRDF\u6a21\u5f0f", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u5730\u8868\u9ad8\u5ea6", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"km", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"DISORT", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"\u500d\u52a0-\u7d2f\u52a0\u6cd5", None))

        self.sp_comboBox_resolution.setItemText(0, QCoreApplication.translate("MainWindow", u"0.5", None))
        self.sp_comboBox_resolution.setItemText(1, QCoreApplication.translate("MainWindow", u"0.1", None))
        self.sp_comboBox_resolution.setItemText(2, QCoreApplication.translate("MainWindow", u"0.05", None))
        self.sp_comboBox_resolution.setItemText(3, QCoreApplication.translate("MainWindow", u"0.01", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u5149\u8c31\u5206\u8fa8\u7387", None))
        self.sp_lineEdit_wavmax.setText(QCoreApplication.translate("MainWindow", u"600", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u900f\u8fc7\u7387\u8ba1\u7b97\u6a21\u5f0f", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u6bb5\u8303\u56f4", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"DISORT\u6d41\u6570", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u8f90\u5c04\u6a21\u578b", None))
        self.sp_comboBox_streams.setItemText(0, QCoreApplication.translate("MainWindow", u"32", None))
        self.sp_comboBox_streams.setItemText(1, QCoreApplication.translate("MainWindow", u"24", None))
        self.sp_comboBox_streams.setItemText(2, QCoreApplication.translate("MainWindow", u"12", None))
        self.sp_comboBox_streams.setItemText(3, QCoreApplication.translate("MainWindow", u"8", None))

        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9010\u7ebf\u79ef\u5206\u65b9\u6cd5", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5e26\u6a21\u5f0f", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"k-\u5206\u5e03\u6cd5", None))

        self.sp_lineEdit_wavmin.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u8bbe", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u4e09", None))
        self.atm.setText(QCoreApplication.translate("MainWindow", u"\u6c14", None))
        self.cloud.setText(QCoreApplication.translate("MainWindow", u"\u4e91", None))
        self.geo.setText(QCoreApplication.translate("MainWindow", u"\u89c6", None))
        self.surface.setText(QCoreApplication.translate("MainWindow", u"\u5730", None))
        self.spectral.setText(QCoreApplication.translate("MainWindow", u"\u5149", None))
        self.putout.setText(QCoreApplication.translate("MainWindow", u"\u51fa", None))
        self.pushButton_atm.setText(QCoreApplication.translate("MainWindow", u"\u6c14", None))
        self.pushButton_cloud.setText(QCoreApplication.translate("MainWindow", u"\u4e91", None))
        self.pushButton_geo.setText(QCoreApplication.translate("MainWindow", u"\u89c6", None))
        self.pushButton_surface.setText(QCoreApplication.translate("MainWindow", u"\u5730", None))
        self.pushButton_spectral.setText(QCoreApplication.translate("MainWindow", u"\u5149", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u51fa", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u8bbe", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u4e09", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165", None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
    # retranslateUi

