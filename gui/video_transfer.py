# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video_transfer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VideoTransfer(object):
    def setupUi(self, VideoTransfer):
        VideoTransfer.setObjectName("VideoTransfer")
        VideoTransfer.resize(623, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(VideoTransfer)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 501, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.select_video = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.select_video.setObjectName("select_video")
        self.verticalLayout_3.addWidget(self.select_video)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.select_style = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.select_style.setObjectName("select_style")
        self.verticalLayout_2.addWidget(self.select_style)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.transfer = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.transfer.setAutoDefault(False)
        self.transfer.setDefault(True)
        self.transfer.setObjectName("transfer")
        self.verticalLayout.addWidget(self.transfer)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.cancel = QtWidgets.QPushButton(VideoTransfer)
        self.cancel.setGeometry(QtCore.QRect(270, 250, 112, 32))
        self.cancel.setAutoDefault(False)
        self.cancel.setDefault(True)
        self.cancel.setObjectName("cancel")

        self.retranslateUi(VideoTransfer)
        QtCore.QMetaObject.connectSlotsByName(VideoTransfer)

    def retranslateUi(self, VideoTransfer):
        _translate = QtCore.QCoreApplication.translate
        VideoTransfer.setWindowTitle(_translate("VideoTransfer", "视频风格迁移"))
        self.select_video.setText(_translate("VideoTransfer", "选择视频"))
        self.select_style.setText(_translate("VideoTransfer", "选择风格"))
        self.transfer.setText(_translate("VideoTransfer", "风格迁移"))
        self.cancel.setText(_translate("VideoTransfer", "返回"))

