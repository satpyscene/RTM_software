# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputsetfour_surface.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget_surface(object):
    def setupUi(self, Widget_surface):
        if not Widget_surface.objectName():
            Widget_surface.setObjectName(u"Widget_surface")
        Widget_surface.resize(401, 300)
        self.verticalLayoutWidget = QWidget(Widget_surface)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 20, 268, 215))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 3)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 0))

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.surface_lineEdit_TEMP = QLineEdit(self.verticalLayoutWidget)
        self.surface_lineEdit_TEMP.setObjectName(u"surface_lineEdit_TEMP")

        self.gridLayout.addWidget(self.surface_lineEdit_TEMP, 2, 2, 1, 1)

        self.radioButton = QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.gridLayout.addWidget(self.radioButton, 2, 3, 1, 1)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 2, 4, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 2, 4, 1, 1)

        self.comboBox_3 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_3.addWidget(self.comboBox_3, 2, 1, 1, 2)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.surface_lineEdit_reflection = QLineEdit(self.verticalLayoutWidget)
        self.surface_lineEdit_reflection.setObjectName(u"surface_lineEdit_reflection")

        self.gridLayout_3.addWidget(self.surface_lineEdit_reflection, 0, 1, 1, 2)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 3, 1, 1)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 5, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 3, 1, 1)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 1, 1, 1, 2)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 4, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 2, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 2)
        self.gridLayout_3.setColumnStretch(2, 2)

        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.surface_pushButton_ok = QPushButton(self.verticalLayoutWidget)
        self.surface_pushButton_ok.setObjectName(u"surface_pushButton_ok")

        self.horizontalLayout.addWidget(self.surface_pushButton_ok)

        self.surface_pushButton_cancel = QPushButton(self.verticalLayoutWidget)
        self.surface_pushButton_cancel.setObjectName(u"surface_pushButton_cancel")

        self.horizontalLayout.addWidget(self.surface_pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget_surface)

        QMetaObject.connectSlotsByName(Widget_surface)
    # setupUi

    def retranslateUi(self, Widget_surface):
        Widget_surface.setWindowTitle(QCoreApplication.translate("Widget_surface", u"\u5730\u8868\u53c2\u6570\u8bbe\u7f6e", None))
        self.label.setText(QCoreApplication.translate("Widget_surface", u"\u5730\u8868\u7c7b\u578b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget_surface", u"\u6717\u4f2f\u4f53", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget_surface", u"\u6052\u5b9a\u53cd\u5c04\u7387", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget_surface", u"BRDF", None))

        self.label_2.setText(QCoreApplication.translate("Widget_surface", u"\u5730\u8868\u6e29\u5ea6", None))
        self.surface_lineEdit_TEMP.setText(QCoreApplication.translate("Widget_surface", u"273", None))
        self.radioButton.setText(QCoreApplication.translate("Widget_surface", u"K", None))
        self.radioButton_2.setText(QCoreApplication.translate("Widget_surface", u"^\u3002C", None))
        self.label_3.setText(QCoreApplication.translate("Widget_surface", u"\u5730\u8868\u53cd\u5c04\u7387", None))
        self.label_4.setText(QCoreApplication.translate("Widget_surface", u"\u6717\u4f2f\u4f53\u7c7b\u578b", None))
        self.label_6.setText(QCoreApplication.translate("Widget_surface", u"BRDF\u6a21\u5f0f", None))
        self.surface_lineEdit_reflection.setText(QCoreApplication.translate("Widget_surface", u"0.02", None))
        self.label_7.setText(QCoreApplication.translate("Widget_surface", u"\u5730\u8868\u9ad8\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("Widget_surface", u"km", None))
        self.label_5.setText(QCoreApplication.translate("Widget_surface", u"LOS\u6307\u6570", None))
        self.surface_pushButton_ok.setText(QCoreApplication.translate("Widget_surface", u"\u5b8c\u6210", None))
        self.surface_pushButton_cancel.setText(QCoreApplication.translate("Widget_surface", u"\u53d6\u6d88", None))
    # retranslateUi

