# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'digitui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 533)
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setContentsMargins(10, 10, -1, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_4.addWidget(self.startButton, 0, QtCore.Qt.AlignLeft)
        self.endButton = QtWidgets.QPushButton(Form)
        self.endButton.setObjectName("endButton")
        self.horizontalLayout_4.addWidget(self.endButton, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_11.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton8 = QtWidgets.QRadioButton(Form)
        self.radioButton8.setObjectName("radioButton8")
        self.horizontalLayout_5.addWidget(self.radioButton8, 0, QtCore.Qt.AlignLeft)
        self.radioButton9 = QtWidgets.QRadioButton(Form)
        self.radioButton9.setObjectName("radioButton9")
        self.horizontalLayout_5.addWidget(self.radioButton9, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_11.addWidget(self.label_9)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lcdNumber_i_8 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_8.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_8.setSizePolicy(sizePolicy)
        self.lcdNumber_i_8.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_8.setDigitCount(1)
        self.lcdNumber_i_8.setObjectName("lcdNumber_i_8")
        self.lcdNumber_i_8.setProperty("intValue", 4)
        self.gridLayout_6.addWidget(self.lcdNumber_i_8, 3, 3, 1, 1)
        self.lcdNumber_i_7 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_7.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_7.setSizePolicy(sizePolicy)
        self.lcdNumber_i_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_7.setDigitCount(1)
        self.lcdNumber_i_7.setProperty("intValue", 3)
        self.lcdNumber_i_7.setObjectName("lcdNumber_i_7")
        self.gridLayout_6.addWidget(self.lcdNumber_i_7, 3, 2, 1, 1)
        self.lcdNumber_i_0 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_0.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_0.setSizePolicy(sizePolicy)
        self.lcdNumber_i_0.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_0.setDigitCount(1)
        self.lcdNumber_i_0.setProperty("intValue", 5)
        self.lcdNumber_i_0.setObjectName("lcdNumber_i_0")
        self.gridLayout_6.addWidget(self.lcdNumber_i_0, 0, 0, 1, 1)
        self.lcdNumber_i_1 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_1.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_1.setSizePolicy(sizePolicy)
        self.lcdNumber_i_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_1.setDigitCount(1)
        self.lcdNumber_i_1.setProperty("intValue", 6)
        self.lcdNumber_i_1.setObjectName("lcdNumber_i_1")
        self.gridLayout_6.addWidget(self.lcdNumber_i_1, 0, 2, 1, 1)
        self.lcdNumber_i_2 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_2.setSizePolicy(sizePolicy)
        self.lcdNumber_i_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_2.setDigitCount(1)
        self.lcdNumber_i_2.setProperty("intValue", 7)
        self.lcdNumber_i_2.setObjectName("lcdNumber_i_2")
        self.gridLayout_6.addWidget(self.lcdNumber_i_2, 0, 3, 1, 1)
        self.lcdNumber_i_3 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_3.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_3.setSizePolicy(sizePolicy)
        self.lcdNumber_i_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_3.setDigitCount(1)
        self.lcdNumber_i_3.setProperty("intValue", 8)
        self.lcdNumber_i_3.setObjectName("lcdNumber_i_3")
        self.gridLayout_6.addWidget(self.lcdNumber_i_3, 1, 0, 1, 1)
        self.lcdNumber_i_4 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_4.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_4.setSizePolicy(sizePolicy)
        self.lcdNumber_i_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_4.setDigitCount(1)
        self.lcdNumber_i_4.setProperty("intValue", 0)
        self.lcdNumber_i_4.setObjectName("lcdNumber_i_4")
        self.gridLayout_6.addWidget(self.lcdNumber_i_4, 1, 2, 1, 1)
        self.lcdNumber_i_5 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_5.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_5.setSizePolicy(sizePolicy)
        self.lcdNumber_i_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_5.setDigitCount(1)
        self.lcdNumber_i_5.setProperty("intValue", 2)
        self.lcdNumber_i_5.setObjectName("lcdNumber_i_5")
        self.gridLayout_6.addWidget(self.lcdNumber_i_5, 1, 3, 1, 1)
        self.lcdNumber_i_6 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_i_6.sizePolicy().hasHeightForWidth())
        self.lcdNumber_i_6.setSizePolicy(sizePolicy)
        self.lcdNumber_i_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_i_6.setDigitCount(1)
        self.lcdNumber_i_6.setProperty("intValue", 1)
        self.lcdNumber_i_6.setObjectName("lcdNumber_i_6")
        self.gridLayout_6.addWidget(self.lcdNumber_i_6, 3, 0, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_6)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_10.setObjectName("label_10")
        self.verticalLayout_11.addWidget(self.label_10)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lcdNumber_f_6 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_6.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_6.setSizePolicy(sizePolicy)
        self.lcdNumber_f_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_6.setDigitCount(1)
        self.lcdNumber_f_6.setProperty("intValue", 7)
        self.lcdNumber_f_6.setObjectName("lcdNumber_f_6")
        self.gridLayout_7.addWidget(self.lcdNumber_f_6, 2, 0, 1, 1)
        self.lcdNumber_f_3 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_3.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_3.setSizePolicy(sizePolicy)
        self.lcdNumber_f_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_3.setDigitCount(1)
        self.lcdNumber_f_3.setProperty("intValue", 8)
        self.lcdNumber_f_3.setObjectName("lcdNumber_f_3")
        self.gridLayout_7.addWidget(self.lcdNumber_f_3, 1, 0, 1, 1)
        self.lcdNumber_f_4 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_4.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_4.setSizePolicy(sizePolicy)
        self.lcdNumber_f_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_4.setDigitCount(1)
        self.lcdNumber_f_4.setObjectName("lcdNumber_f_4")
        self.gridLayout_7.addWidget(self.lcdNumber_f_4, 1, 1, 1, 1)
        self.lcdNumber_f_0 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_0.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_0.setSizePolicy(sizePolicy)
        self.lcdNumber_f_0.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_0.setDigitCount(1)
        self.lcdNumber_f_0.setProperty("intValue", 1)
        self.lcdNumber_f_0.setObjectName("lcdNumber_f_0")
        self.gridLayout_7.addWidget(self.lcdNumber_f_0, 0, 0, 1, 1)
        self.lcdNumber_f_5 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_5.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_5.setSizePolicy(sizePolicy)
        self.lcdNumber_f_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_5.setDigitCount(1)
        self.lcdNumber_f_5.setProperty("intValue", 4)
        self.lcdNumber_f_5.setObjectName("lcdNumber_f_5")
        self.gridLayout_7.addWidget(self.lcdNumber_f_5, 1, 2, 1, 1)
        self.lcdNumber_f_1 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_1.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_1.setSizePolicy(sizePolicy)
        self.lcdNumber_f_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_1.setDigitCount(1)
        self.lcdNumber_f_1.setProperty("intValue", 2)
        self.lcdNumber_f_1.setObjectName("lcdNumber_f_1")
        self.gridLayout_7.addWidget(self.lcdNumber_f_1, 0, 1, 1, 1)
        self.lcdNumber_f_2 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_2.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_2.setSizePolicy(sizePolicy)
        self.lcdNumber_f_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_2.setDigitCount(1)
        self.lcdNumber_f_2.setProperty("intValue", 3)
        self.lcdNumber_f_2.setObjectName("lcdNumber_f_2")
        self.gridLayout_7.addWidget(self.lcdNumber_f_2, 0, 2, 1, 1)
        self.lcdNumber_f_7 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_7.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_7.setSizePolicy(sizePolicy)
        self.lcdNumber_f_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_7.setDigitCount(1)
        self.lcdNumber_f_7.setProperty("intValue", 6)
        self.lcdNumber_f_7.setObjectName("lcdNumber_f_7")
        self.gridLayout_7.addWidget(self.lcdNumber_f_7, 2, 1, 1, 1)
        self.lcdNumber_f_8 = QtWidgets.QLCDNumber(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_f_8.sizePolicy().hasHeightForWidth())
        self.lcdNumber_f_8.setSizePolicy(sizePolicy)
        self.lcdNumber_f_8.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lcdNumber_f_8.setDigitCount(1)
        self.lcdNumber_f_8.setProperty("intValue", 5)
        self.lcdNumber_f_8.setObjectName("lcdNumber_f_8")
        self.gridLayout_7.addWidget(self.lcdNumber_f_8, 2, 2, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_7)
        self.listWidget = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(300, 217))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_11.addWidget(self.listWidget)
        self.gridLayout_5.addLayout(self.verticalLayout_11, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(100, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(100, 30))
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.label_7 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber_1_8 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_8.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_1_8.setDigitCount(1)
        self.lcdNumber_1_8.setObjectName("lcdNumber_1_8")
        self.gridLayout.addWidget(self.lcdNumber_1_8, 2, 2, 1, 1)
        self.lcdNumber_1_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_2.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_1_2.setDigitCount(1)
        self.lcdNumber_1_2.setObjectName("lcdNumber_1_2")
        self.gridLayout.addWidget(self.lcdNumber_1_2, 0, 2, 1, 1)
        self.lcdNumber_1_3 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_3.setMinimumSize(QtCore.QSize(64, 75))
        self.lcdNumber_1_3.setDigitCount(1)
        self.lcdNumber_1_3.setObjectName("lcdNumber_1_3")
        self.gridLayout.addWidget(self.lcdNumber_1_3, 1, 0, 1, 1)
        self.lcdNumber_1_5 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_5.setMinimumSize(QtCore.QSize(64, 75))
        self.lcdNumber_1_5.setDigitCount(1)
        self.lcdNumber_1_5.setProperty("intValue", 0)
        self.lcdNumber_1_5.setObjectName("lcdNumber_1_5")
        self.gridLayout.addWidget(self.lcdNumber_1_5, 1, 2, 1, 1)
        self.lcdNumber_1_6 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_6.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_1_6.setDigitCount(1)
        self.lcdNumber_1_6.setObjectName("lcdNumber_1_6")
        self.gridLayout.addWidget(self.lcdNumber_1_6, 2, 0, 1, 1)
        self.lcdNumber_1_4 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_4.setMinimumSize(QtCore.QSize(64, 75))
        self.lcdNumber_1_4.setDigitCount(1)
        self.lcdNumber_1_4.setObjectName("lcdNumber_1_4")
        self.gridLayout.addWidget(self.lcdNumber_1_4, 1, 1, 1, 1)
        self.lcdNumber_1_7 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_7.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_1_7.setDigitCount(1)
        self.lcdNumber_1_7.setObjectName("lcdNumber_1_7")
        self.gridLayout.addWidget(self.lcdNumber_1_7, 2, 1, 1, 1)
        self.lcdNumber_1_1 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_1.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_1_1.setDigitCount(1)
        self.lcdNumber_1_1.setObjectName("lcdNumber_1_1")
        self.gridLayout.addWidget(self.lcdNumber_1_1, 0, 1, 1, 1)
        self.lcdNumber_1_0 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_1_0.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_1_0.setDigitCount(1)
        self.lcdNumber_1_0.setObjectName("lcdNumber_1_0")
        self.gridLayout.addWidget(self.lcdNumber_1_0, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_9.addWidget(self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_9.addWidget(self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_9.addWidget(self.lineEdit_6)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lcdNumber_2_3 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_3.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_3.setDigitCount(1)
        self.lcdNumber_2_3.setObjectName("lcdNumber_2_3")
        self.gridLayout_4.addWidget(self.lcdNumber_2_3, 1, 0, 1, 1)
        self.lcdNumber_2_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_2.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_2.setDigitCount(1)
        self.lcdNumber_2_2.setObjectName("lcdNumber_2_2")
        self.gridLayout_4.addWidget(self.lcdNumber_2_2, 0, 2, 1, 1)
        self.lcdNumber_2_0 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_0.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_0.setDigitCount(1)
        self.lcdNumber_2_0.setObjectName("lcdNumber_2_0")
        self.gridLayout_4.addWidget(self.lcdNumber_2_0, 0, 0, 1, 1)
        self.lcdNumber_2_1 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_1.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_1.setDigitCount(1)
        self.lcdNumber_2_1.setObjectName("lcdNumber_2_1")
        self.gridLayout_4.addWidget(self.lcdNumber_2_1, 0, 1, 1, 1)
        self.lcdNumber_2_6 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_6.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_6.setDigitCount(1)
        self.lcdNumber_2_6.setObjectName("lcdNumber_2_6")
        self.gridLayout_4.addWidget(self.lcdNumber_2_6, 2, 0, 1, 1)
        self.lcdNumber_2_4 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_4.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_4.setDigitCount(1)
        self.lcdNumber_2_4.setObjectName("lcdNumber_2_4")
        self.gridLayout_4.addWidget(self.lcdNumber_2_4, 1, 1, 1, 1)
        self.lcdNumber_2_5 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_5.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_5.setDigitCount(1)
        self.lcdNumber_2_5.setObjectName("lcdNumber_2_5")
        self.gridLayout_4.addWidget(self.lcdNumber_2_5, 1, 2, 1, 1)
        self.lcdNumber_2_7 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_7.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_7.setDigitCount(1)
        self.lcdNumber_2_7.setObjectName("lcdNumber_2_7")
        self.gridLayout_4.addWidget(self.lcdNumber_2_7, 2, 1, 1, 1)
        self.lcdNumber_2_8 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2_8.setMinimumSize(QtCore.QSize(64, 74))
        self.lcdNumber_2_8.setDigitCount(1)
        self.lcdNumber_2_8.setObjectName("lcdNumber_2_8")
        self.gridLayout_4.addWidget(self.lcdNumber_2_8, 2, 2, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(600, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_10.addWidget(self.widget)
        self.gridLayout_5.addLayout(self.verticalLayout_10, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 3, 1, 1)

        self.retranslateUi(Form)
        self.startButton.clicked.connect(self.lineEdit_2.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数码问题"))
        self.startButton.setText(_translate("Form", "开始"))
        self.endButton.setText(_translate("Form", "结束"))
        self.radioButton8.setText(_translate("Form", "八数码"))
        self.radioButton9.setText(_translate("Form", "九数码"))
        self.label_9.setText(_translate("Form", "起始状态"))
        self.label_10.setText(_translate("Form", "终止状态"))
        self.label_2.setText(_translate("Form", "h1当前最小结点"))
        self.label.setText(_translate("Form", "OPEN表结点数"))
        self.label_7.setText(_translate("Form", "总拓展结点数"))
        self.label_3.setText(_translate("Form", "最小结点评估值"))
        self.label_4.setText(_translate("Form", "h2当前最小结点"))
        self.label_5.setText(_translate("Form", "OPEN表结点数"))
        self.label_6.setText(_translate("Form", "总拓展结点数"))
        self.label_8.setText(_translate("Form", "最小结点评估值"))

