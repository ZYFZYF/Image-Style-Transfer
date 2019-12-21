# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_video.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectVideo(object):
    def setupUi(self, SelectVideo):
        SelectVideo.setObjectName("SelectVideo")
        SelectVideo.resize(400, 300)
        self.select_camera = QtWidgets.QPushButton(SelectVideo)
        self.select_camera.setGeometry(QtCore.QRect(140, 70, 112, 32))
        self.select_camera.setAutoDefault(True)
        self.select_camera.setDefault(False)
        self.select_camera.setObjectName("select_camera")
        self.select_file = QtWidgets.QPushButton(SelectVideo)
        self.select_file.setGeometry(QtCore.QRect(140, 140, 112, 32))
        self.select_file.setAutoDefault(True)
        self.select_file.setDefault(False)
        self.select_file.setObjectName("select_file")
        self.cancel = QtWidgets.QPushButton(SelectVideo)
        self.cancel.setGeometry(QtCore.QRect(140, 210, 112, 32))
        self.cancel.setDefault(True)
        self.cancel.setObjectName("cancel")

        self.retranslateUi(SelectVideo)
        QtCore.QMetaObject.connectSlotsByName(SelectVideo)

    def retranslateUi(self, SelectVideo):
        _translate = QtCore.QCoreApplication.translate
        SelectVideo.setWindowTitle(_translate("SelectVideo", "选择视频来源"))
        self.select_camera.setText(_translate("SelectVideo", "从摄像头获取"))
        self.select_file.setText(_translate("SelectVideo", "从文件选择"))
        self.cancel.setText(_translate("SelectVideo", "返回"))

