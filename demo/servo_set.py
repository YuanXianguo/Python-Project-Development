# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servo_set.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServoSet(object):
    def setupUi(self, ServoSet):
        ServoSet.setObjectName("ServoSet")
        ServoSet.resize(499, 344)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ServoSet)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lab_0 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_0.sizePolicy().hasHeightForWidth())
        self.lab_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lab_0.setFont(font)
        self.lab_0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_0.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.lab_0.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_0.setObjectName("lab_0")
        self.gridLayout.addWidget(self.lab_0, 0, 0, 1, 1)
        self.lineEdit_servo_1 = QtWidgets.QLineEdit(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_servo_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_servo_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_servo_1.setFont(font)
        self.lineEdit_servo_1.setObjectName("lineEdit_servo_1")
        self.gridLayout.addWidget(self.lineEdit_servo_1, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(ServoSet)
        self.label.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.lab_1 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_1.sizePolicy().hasHeightForWidth())
        self.lab_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lab_1.setFont(font)
        self.lab_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_1.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.lab_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_1.setObjectName("lab_1")
        self.gridLayout.addWidget(self.lab_1, 1, 0, 1, 1)
        self.lineEdit_servo_2 = QtWidgets.QLineEdit(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_servo_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_servo_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_servo_2.setFont(font)
        self.lineEdit_servo_2.setObjectName("lineEdit_servo_2")
        self.gridLayout.addWidget(self.lineEdit_servo_2, 1, 1, 1, 1)
        self.label_1188 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1188.sizePolicy().hasHeightForWidth())
        self.label_1188.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1188.setFont(font)
        self.label_1188.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_1188.setObjectName("label_1188")
        self.gridLayout.addWidget(self.label_1188, 1, 2, 1, 1)
        self.lab_2 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_2.sizePolicy().hasHeightForWidth())
        self.lab_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lab_2.setFont(font)
        self.lab_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_2.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.lab_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_2.setObjectName("lab_2")
        self.gridLayout.addWidget(self.lab_2, 2, 0, 1, 1)
        self.lineEdit_servo_3 = QtWidgets.QLineEdit(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_servo_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_servo_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_servo_3.setFont(font)
        self.lineEdit_servo_3.setObjectName("lineEdit_servo_3")
        self.gridLayout.addWidget(self.lineEdit_servo_3, 2, 1, 1, 1)
        self.label_1190 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1190.sizePolicy().hasHeightForWidth())
        self.label_1190.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1190.setFont(font)
        self.label_1190.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_1190.setObjectName("label_1190")
        self.gridLayout.addWidget(self.label_1190, 2, 2, 1, 1)
        self.lab_3 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_3.sizePolicy().hasHeightForWidth())
        self.lab_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lab_3.setFont(font)
        self.lab_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_3.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.lab_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_3.setObjectName("lab_3")
        self.gridLayout.addWidget(self.lab_3, 3, 0, 1, 1)
        self.lineEdit_servo_4 = QtWidgets.QLineEdit(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_servo_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_servo_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_servo_4.setFont(font)
        self.lineEdit_servo_4.setObjectName("lineEdit_servo_4")
        self.gridLayout.addWidget(self.lineEdit_servo_4, 3, 1, 1, 1)
        self.label_1192 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1192.sizePolicy().hasHeightForWidth())
        self.label_1192.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1192.setFont(font)
        self.label_1192.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_1192.setObjectName("label_1192")
        self.gridLayout.addWidget(self.label_1192, 3, 2, 1, 1)
        self.lab_4 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_4.sizePolicy().hasHeightForWidth())
        self.lab_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lab_4.setFont(font)
        self.lab_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lab_4.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.lab_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lab_4.setObjectName("lab_4")
        self.gridLayout.addWidget(self.lab_4, 4, 0, 1, 1)
        self.lineEdit_servo_5 = QtWidgets.QLineEdit(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_servo_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_servo_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_servo_5.setFont(font)
        self.lineEdit_servo_5.setObjectName("lineEdit_servo_5")
        self.gridLayout.addWidget(self.lineEdit_servo_5, 4, 1, 1, 1)
        self.label_1193 = QtWidgets.QLabel(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1193.sizePolicy().hasHeightForWidth())
        self.label_1193.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_1193.setFont(font)
        self.label_1193.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.label_1193.setObjectName("label_1193")
        self.gridLayout.addWidget(self.label_1193, 4, 2, 1, 1)
        self.btn_servo_1 = QtWidgets.QPushButton(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_servo_1.sizePolicy().hasHeightForWidth())
        self.btn_servo_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servo_1.setFont(font)
        self.btn_servo_1.setObjectName("btn_servo_1")
        self.gridLayout.addWidget(self.btn_servo_1, 5, 0, 1, 1)
        self.btn_servo_2 = QtWidgets.QPushButton(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_servo_2.sizePolicy().hasHeightForWidth())
        self.btn_servo_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servo_2.setFont(font)
        self.btn_servo_2.setObjectName("btn_servo_2")
        self.gridLayout.addWidget(self.btn_servo_2, 5, 1, 1, 1)
        self.btn_servo_0 = QtWidgets.QPushButton(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_servo_0.sizePolicy().hasHeightForWidth())
        self.btn_servo_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servo_0.setFont(font)
        self.btn_servo_0.setObjectName("btn_servo_0")
        self.gridLayout.addWidget(self.btn_servo_0, 5, 2, 1, 1)
        self.btn_servo_4 = QtWidgets.QPushButton(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_servo_4.sizePolicy().hasHeightForWidth())
        self.btn_servo_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servo_4.setFont(font)
        self.btn_servo_4.setObjectName("btn_servo_4")
        self.gridLayout.addWidget(self.btn_servo_4, 6, 0, 1, 1)
        self.btn_servo_5 = QtWidgets.QPushButton(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_servo_5.sizePolicy().hasHeightForWidth())
        self.btn_servo_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servo_5.setFont(font)
        self.btn_servo_5.setObjectName("btn_servo_5")
        self.gridLayout.addWidget(self.btn_servo_5, 6, 1, 1, 1)
        self.btn_servo_3 = QtWidgets.QPushButton(ServoSet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_servo_3.sizePolicy().hasHeightForWidth())
        self.btn_servo_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_servo_3.setFont(font)
        self.btn_servo_3.setObjectName("btn_servo_3")
        self.gridLayout.addWidget(self.btn_servo_3, 6, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(ServoSet)
        QtCore.QMetaObject.connectSlotsByName(ServoSet)

    def retranslateUi(self, ServoSet):
        _translate = QtCore.QCoreApplication.translate
        ServoSet.setWindowTitle(_translate("ServoSet", "Form"))
        self.lab_0.setText(_translate("ServoSet", "机械齿轮"))
        self.lab_1.setText(_translate("ServoSet", "伺服速度"))
        self.label_1188.setText(_translate("ServoSet", "r/S"))
        self.lab_2.setText(_translate("ServoSet", "打开转矩"))
        self.label_1190.setText(_translate("ServoSet", "N.M"))
        self.lab_3.setText(_translate("ServoSet", "关闭转矩"))
        self.label_1192.setText(_translate("ServoSet", "N.M"))
        self.lab_4.setText(_translate("ServoSet", "打开角度"))
        self.label_1193.setText(_translate("ServoSet", "°"))
        self.btn_servo_1.setText(_translate("ServoSet", "伺服启动"))
        self.btn_servo_2.setText(_translate("ServoSet", "伺服停止"))
        self.btn_servo_0.setText(_translate("ServoSet", "伺服归零"))
        self.btn_servo_4.setText(_translate("ServoSet", "正向点动"))
        self.btn_servo_5.setText(_translate("ServoSet", "反向点动"))
        self.btn_servo_3.setText(_translate("ServoSet", "故障复位"))

