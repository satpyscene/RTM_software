# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'parameter_pop.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_widgettestpop(object):
    def setupUi(self, widgettestpop):
        if not widgettestpop.objectName():
            widgettestpop.setObjectName(u"widgettestpop")
        widgettestpop.resize(711, 360)
        self.frame = QFrame(widgettestpop)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 20, 631, 331))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 40, 591, 281))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 30, 151, 188))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 4, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout.addWidget(self.comboBox_3, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(50, 30, 151, 188))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 0, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 2, 1, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 5, 0, 1, 1)

        self.comboBox_4 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_2.addWidget(self.comboBox_4, 3, 1, 1, 1)

        self.comboBox_5 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_2.addWidget(self.comboBox_5, 4, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_2.addWidget(self.comboBox_6, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(190, 30, 151, 188))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_3.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 0, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 4, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 0, 0, 1, 1)

        self.lineEdit_9 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_3.addWidget(self.lineEdit_9, 2, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 5, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_3.addWidget(self.comboBox_7, 3, 1, 1, 1)

        self.comboBox_8 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_3.addWidget(self.comboBox_8, 4, 1, 1, 1)

        self.comboBox_9 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout_3.addWidget(self.comboBox_9, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(200, 30, 151, 188))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.gridLayoutWidget_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_4.addWidget(self.lineEdit_10, 1, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_4.addWidget(self.lineEdit_11, 0, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 4, 0, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_4.addWidget(self.label_22, 0, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_4.addWidget(self.lineEdit_12, 2, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_4.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 5, 0, 1, 1)

        self.comboBox_10 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.gridLayout_4.addWidget(self.comboBox_10, 3, 1, 1, 1)

        self.comboBox_11 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout_4.addWidget(self.comboBox_11, 4, 1, 1, 1)

        self.comboBox_12 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_12.setObjectName(u"comboBox_12")

        self.gridLayout_4.addWidget(self.comboBox_12, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_5 = QWidget(self.tab_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(200, 20, 151, 188))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.gridLayoutWidget_5)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)

        self.lineEdit_13 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_5.addWidget(self.lineEdit_13, 1, 1, 1, 1)

        self.lineEdit_14 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_5.addWidget(self.lineEdit_14, 0, 1, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_5)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_5.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_5)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_5.addWidget(self.label_27, 4, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_5)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 0, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_5.addWidget(self.lineEdit_15, 2, 1, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_5)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_5.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_30 = QLabel(self.gridLayoutWidget_5)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_5.addWidget(self.label_30, 5, 0, 1, 1)

        self.comboBox_13 = QComboBox(self.gridLayoutWidget_5)
        self.comboBox_13.setObjectName(u"comboBox_13")

        self.gridLayout_5.addWidget(self.comboBox_13, 3, 1, 1, 1)

        self.comboBox_14 = QComboBox(self.gridLayoutWidget_5)
        self.comboBox_14.setObjectName(u"comboBox_14")

        self.gridLayout_5.addWidget(self.comboBox_14, 4, 1, 1, 1)

        self.comboBox_15 = QComboBox(self.gridLayoutWidget_5)
        self.comboBox_15.setObjectName(u"comboBox_15")

        self.gridLayout_5.addWidget(self.comboBox_15, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayoutWidget_6 = QWidget(self.tab_6)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(200, 30, 151, 188))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.gridLayoutWidget_6)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_6.addWidget(self.label_31, 1, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_6.addWidget(self.lineEdit_16, 1, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_6.addWidget(self.lineEdit_17, 0, 1, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_6)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_6.addWidget(self.label_32, 3, 0, 1, 1)

        self.label_33 = QLabel(self.gridLayoutWidget_6)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_6.addWidget(self.label_33, 4, 0, 1, 1)

        self.label_34 = QLabel(self.gridLayoutWidget_6)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_6.addWidget(self.label_34, 0, 0, 1, 1)

        self.lineEdit_18 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_6.addWidget(self.lineEdit_18, 2, 1, 1, 1)

        self.label_35 = QLabel(self.gridLayoutWidget_6)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_6.addWidget(self.label_35, 2, 0, 1, 1)

        self.label_36 = QLabel(self.gridLayoutWidget_6)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 5, 0, 1, 1)

        self.comboBox_16 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_16.setObjectName(u"comboBox_16")

        self.gridLayout_6.addWidget(self.comboBox_16, 3, 1, 1, 1)

        self.comboBox_17 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_17.setObjectName(u"comboBox_17")

        self.gridLayout_6.addWidget(self.comboBox_17, 4, 1, 1, 1)

        self.comboBox_18 = QComboBox(self.gridLayoutWidget_6)
        self.comboBox_18.setObjectName(u"comboBox_18")

        self.gridLayout_6.addWidget(self.comboBox_18, 5, 1, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.pushButton_closeparameterpop = QPushButton(self.frame)
        self.pushButton_closeparameterpop.setObjectName(u"pushButton_closeparameterpop")
        self.pushButton_closeparameterpop.setGeometry(QRect(480, 10, 101, 31))

        self.retranslateUi(widgettestpop)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(widgettestpop)
    # setupUi

    def retranslateUi(self, widgettestpop):
        widgettestpop.setWindowTitle(QCoreApplication.translate("widgettestpop", u"testpop", None))
        self.label_2.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("widgettestpop", u"\u8fd0\u884c\u53c2\u6570", None))
        self.label_7.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("widgettestpop", u"\u4f20\u611f\u5668\u53c2\u6570", None))
        self.label_13.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_15.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_18.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("widgettestpop", u"\u5927\u6c14\u53c2\u6570", None))
        self.label_19.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_20.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_21.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_22.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_23.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_24.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("widgettestpop", u"\u89c2\u6d4b\u51e0\u4f55\u53c2\u6570", None))
        self.label_25.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_26.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("widgettestpop", u"\u5730\u8868\u53c2\u6570", None))
        self.label_31.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_34.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("widgettestpop", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("widgettestpop", u"\u8f93\u51fa\u53c2\u6570", None))
        self.pushButton_closeparameterpop.setText(QCoreApplication.translate("widgettestpop", u"\u5173\u95ed", None))
    # retranslateUi

