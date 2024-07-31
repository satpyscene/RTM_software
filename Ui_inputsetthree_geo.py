# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inputsetthree_geo.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGraphicsView, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Widget_geo(object):
    def setupUi(self, Widget_geo):
        if not Widget_geo.objectName():
            Widget_geo.setObjectName(u"Widget_geo")
        Widget_geo.resize(397, 301)
        self.gridLayoutWidget_3 = QWidget(Widget_geo)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 10, 371, 289))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.geo_lineEdit_angel = QLineEdit(self.gridLayoutWidget_3)
        self.geo_lineEdit_angel.setObjectName(u"geo_lineEdit_angel")

        self.gridLayout.addWidget(self.geo_lineEdit_angel, 3, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.line = QFrame(self.gridLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 5, 0, 1, 2)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.gridLayoutWidget_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_3.addWidget(self.graphicsView, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 3, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_2.addWidget(self.lineEdit_6, 1, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_2.addWidget(self.lineEdit_7, 1, 5, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 4, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_2.addWidget(self.checkBox_2, 0, 0, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.geo_pushButton_ok = QPushButton(self.gridLayoutWidget_3)
        self.geo_pushButton_ok.setObjectName(u"geo_pushButton_ok")

        self.horizontalLayout.addWidget(self.geo_pushButton_ok)

        self.geo_pushButton_cancel = QPushButton(self.gridLayoutWidget_3)
        self.geo_pushButton_cancel.setObjectName(u"geo_pushButton_cancel")

        self.horizontalLayout.addWidget(self.geo_pushButton_cancel)


        self.gridLayout_3.addLayout(self.horizontalLayout, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.retranslateUi(Widget_geo)

        QMetaObject.connectSlotsByName(Widget_geo)
    # setupUi

    def retranslateUi(self, Widget_geo):
        Widget_geo.setWindowTitle(QCoreApplication.translate("Widget_geo", u"\u51e0\u4f55\u53c2\u6570\u8bbe\u7f6e", None))
        self.checkBox.setText(QCoreApplication.translate("Widget_geo", u"\u5730\u7403\u66f2\u7387", None))
        self.label_2.setText(QCoreApplication.translate("Widget_geo", u"\u89c2\u6d4b\u4f4d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("Widget_geo", u"\u76ee\u6807\u7269\u9ad8\u5ea6", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget_geo", u"\u659c\u7a0b", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget_geo", u"\u6c34\u5e73", None))

        self.geo_lineEdit_angel.setText(QCoreApplication.translate("Widget_geo", u"0", None))
        self.label.setText(QCoreApplication.translate("Widget_geo", u"\u51e0\u4f55\u8def\u5f84", None))
        self.label_4.setText(QCoreApplication.translate("Widget_geo", u"\u89c2\u6d4b/\u76ee\u6807\u5929\u9876\u89d2", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Widget_geo", u"0", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Widget_geo", u"\u5927\u6c14\u9876", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Widget_geo", u"\u5730\u9762", None))

        self.label_5.setText(QCoreApplication.translate("Widget_geo", u"\u65f6\u95f4(UTC)\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Widget_geo", u"xxxxxx", None))
        self.label_6.setText(QCoreApplication.translate("Widget_geo", u"xxxxx", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget_geo", u"\u65e5/\u6708\u51e0\u4f55", None))
        self.geo_pushButton_ok.setText(QCoreApplication.translate("Widget_geo", u"\u5b8c\u6210", None))
        self.geo_pushButton_cancel.setText(QCoreApplication.translate("Widget_geo", u"\u53d6\u6d88", None))
    # retranslateUi

