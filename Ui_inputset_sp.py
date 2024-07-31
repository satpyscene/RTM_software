# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputset_sp.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Widget_spectral(object):
    def setupUi(self, Widget_spectral):
        if not Widget_spectral.objectName():
            Widget_spectral.setObjectName(u"Widget_spectral")
        Widget_spectral.resize(400, 300)
        self.gridLayoutWidget = QWidget(Widget_spectral)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 40, 335, 176))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.sp_lineEdit_wavmax = QLineEdit(self.gridLayoutWidget)
        self.sp_lineEdit_wavmax.setObjectName(u"sp_lineEdit_wavmax")
        self.sp_lineEdit_wavmax.setMinimumSize(QSize(80, 0))
        self.sp_lineEdit_wavmax.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.sp_lineEdit_wavmax, 1, 2, 1, 1)

        self.sp_comboBox_resolution = QComboBox(self.gridLayoutWidget)
        self.sp_comboBox_resolution.addItem("")
        self.sp_comboBox_resolution.addItem("")
        self.sp_comboBox_resolution.addItem("")
        self.sp_comboBox_resolution.addItem("")
        self.sp_comboBox_resolution.setObjectName(u"sp_comboBox_resolution")

        self.gridLayout.addWidget(self.sp_comboBox_resolution, 4, 1, 1, 2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.sp_lineEdit_wavmin = QLineEdit(self.gridLayoutWidget)
        self.sp_lineEdit_wavmin.setObjectName(u"sp_lineEdit_wavmin")
        self.sp_lineEdit_wavmin.setMinimumSize(QSize(80, 0))
        self.sp_lineEdit_wavmin.setMaximumSize(QSize(80, 16777215))

        self.gridLayout.addWidget(self.sp_lineEdit_wavmin, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.sp_comboBox_streams = QComboBox(self.gridLayoutWidget)
        self.sp_comboBox_streams.addItem("")
        self.sp_comboBox_streams.addItem("")
        self.sp_comboBox_streams.addItem("")
        self.sp_comboBox_streams.addItem("")
        self.sp_comboBox_streams.setObjectName(u"sp_comboBox_streams")

        self.gridLayout.addWidget(self.sp_comboBox_streams, 5, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sp_pushButton_ok = QPushButton(self.gridLayoutWidget)
        self.sp_pushButton_ok.setObjectName(u"sp_pushButton_ok")

        self.horizontalLayout.addWidget(self.sp_pushButton_ok)

        self.sp_pushButton_cancel = QPushButton(self.gridLayoutWidget)
        self.sp_pushButton_cancel.setObjectName(u"sp_pushButton_cancel")

        self.horizontalLayout.addWidget(self.sp_pushButton_cancel)


        self.gridLayout.addLayout(self.horizontalLayout, 9, 2, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)


        self.retranslateUi(Widget_spectral)

        QMetaObject.connectSlotsByName(Widget_spectral)
    # setupUi

    def retranslateUi(self, Widget_spectral):
        Widget_spectral.setWindowTitle(QCoreApplication.translate("Widget_spectral", u"\u5149\u8c31\u53c2\u6570\u8bbe\u7f6e", None))
        self.sp_lineEdit_wavmax.setText(QCoreApplication.translate("Widget_spectral", u"600", None))
        self.sp_comboBox_resolution.setItemText(0, QCoreApplication.translate("Widget_spectral", u"0.5", None))
        self.sp_comboBox_resolution.setItemText(1, QCoreApplication.translate("Widget_spectral", u"0.1", None))
        self.sp_comboBox_resolution.setItemText(2, QCoreApplication.translate("Widget_spectral", u"0.05", None))
        self.sp_comboBox_resolution.setItemText(3, QCoreApplication.translate("Widget_spectral", u"0.01", None))

        self.label_4.setText(QCoreApplication.translate("Widget_spectral", u"\u6ce2\u6bb5\u8303\u56f4", None))
        self.sp_lineEdit_wavmin.setText(QCoreApplication.translate("Widget_spectral", u"500", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget_spectral", u"DISORT", None))

        self.sp_comboBox_streams.setItemText(0, QCoreApplication.translate("Widget_spectral", u"32", None))
        self.sp_comboBox_streams.setItemText(1, QCoreApplication.translate("Widget_spectral", u"24", None))
        self.sp_comboBox_streams.setItemText(2, QCoreApplication.translate("Widget_spectral", u"12", None))
        self.sp_comboBox_streams.setItemText(3, QCoreApplication.translate("Widget_spectral", u"8", None))

        self.label.setText(QCoreApplication.translate("Widget_spectral", u"\u8f90\u5c04\u6a21\u578b", None))
        self.sp_pushButton_ok.setText(QCoreApplication.translate("Widget_spectral", u"\u5b8c\u6210", None))
        self.sp_pushButton_cancel.setText(QCoreApplication.translate("Widget_spectral", u"\u53d6\u6d88", None))
        self.label_3.setText(QCoreApplication.translate("Widget_spectral", u"DISORT\u6d41\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Widget_spectral", u"\u5149\u8c31\u5206\u8fa8\u7387", None))
    # retranslateUi

