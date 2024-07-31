# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputsetone_atm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Widget_atm(object):
    def setupUi(self, Widget_atm):
        if not Widget_atm.objectName():
            Widget_atm.setObjectName(u"Widget_atm")
        Widget_atm.resize(405, 300)
        self.gridLayoutWidget = QWidget(Widget_atm)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 20, 321, 261))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.atm_pushButton_ok = QPushButton(self.gridLayoutWidget)
        self.atm_pushButton_ok.setObjectName(u"atm_pushButton_ok")

        self.horizontalLayout.addWidget(self.atm_pushButton_ok)

        self.atm_pushButton_cancel = QPushButton(self.gridLayoutWidget)
        self.atm_pushButton_cancel.setObjectName(u"atm_pushButton_cancel")

        self.horizontalLayout.addWidget(self.atm_pushButton_cancel)


        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.label)

        self.atm_comboBox_model = QComboBox(self.gridLayoutWidget)
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.addItem("")
        self.atm_comboBox_model.setObjectName(u"atm_comboBox_model")

        self.horizontalLayout_2.addWidget(self.atm_comboBox_model)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.gridLayoutWidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(59, 16777215))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(195, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox_2)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 6, 0, 1, 1)


        self.retranslateUi(Widget_atm)

        QMetaObject.connectSlotsByName(Widget_atm)
    # setupUi

    def retranslateUi(self, Widget_atm):
        Widget_atm.setWindowTitle(QCoreApplication.translate("Widget_atm", u"\u5927\u6c14\u53c2\u6570\u8bbe\u7f6e", None))
        self.atm_pushButton_ok.setText(QCoreApplication.translate("Widget_atm", u"\u5b8c\u6210", None))
        self.atm_pushButton_cancel.setText(QCoreApplication.translate("Widget_atm", u"\u53d6\u6d88", None))
        self.label.setText(QCoreApplication.translate("Widget_atm", u"\u5927\u6c14\u6a21\u5f0f", None))
        self.atm_comboBox_model.setItemText(0, QCoreApplication.translate("Widget_atm", u"\u7528\u6237\u81ea\u5b9a\u4e49", None))
        self.atm_comboBox_model.setItemText(1, QCoreApplication.translate("Widget_atm", u"\u70ed\u5e26", None))
        self.atm_comboBox_model.setItemText(2, QCoreApplication.translate("Widget_atm", u"\u4e2d\u7eac\u5ea6\u590f\u5929", None))
        self.atm_comboBox_model.setItemText(3, QCoreApplication.translate("Widget_atm", u"\u4e2d\u7eac\u5ea6\u51ac\u5929", None))
        self.atm_comboBox_model.setItemText(4, QCoreApplication.translate("Widget_atm", u"\u4e9a\u5317\u6781\u590f\u5929", None))
        self.atm_comboBox_model.setItemText(5, QCoreApplication.translate("Widget_atm", u"\u4e9a\u5317\u6781\u51ac\u5929", None))
        self.atm_comboBox_model.setItemText(6, QCoreApplication.translate("Widget_atm", u"\u7f8e\u56fd\u6807\u51c6\u5927\u6c14", None))

        self.label_2.setText(QCoreApplication.translate("Widget_atm", u"\u5ed3\u7ebf\u7c7b\u578b", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Widget_atm", u"\u6e29\u5ea6", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Widget_atm", u"\u6c34\u6c7d", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("Widget_atm", u"\u4e8c\u6c27\u5316\u78b3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("Widget_atm", u"\u81ed\u6c27", None))

        self.pushButton_3.setText(QCoreApplication.translate("Widget_atm", u"\u67e5\u770b", None))
    # retranslateUi

