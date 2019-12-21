# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'start.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(438, 214)
        self.select_image = QtWidgets.QPushButton(StartWindow)
        self.select_image.setGeometry(QtCore.QRect(60, 130, 101, 31))
        self.select_image.setDefault(True)
        self.select_image.setObjectName("select_image")
        self.select_video = QtWidgets.QPushButton(StartWindow)
        self.select_video.setGeometry(QtCore.QRect(260, 130, 112, 32))
        self.select_video.setDefault(True)
        self.select_video.setObjectName("select_video")
        self.label = QtWidgets.QLabel(StartWindow)
        self.label.setGeometry(QtCore.QRect(110, 50, 211, 41))
        self.label.setObjectName("label")

        self.retranslateUi(StartWindow)
        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "风格迁移"))
        self.select_image.setText(_translate("StartWindow", "图像"))
        self.select_video.setText(_translate("StartWindow", "视频"))
        self.label.setText(_translate("StartWindow", "请选择您要进行风格迁移的对象"))

