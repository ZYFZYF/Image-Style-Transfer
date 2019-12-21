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
        VideoTransfer.resize(868, 460)
        self.cancel = QtWidgets.QPushButton(VideoTransfer)
        self.cancel.setGeometry(QtCore.QRect(370, 400, 112, 32))
        self.cancel.setAutoDefault(False)
        self.cancel.setDefault(True)
        self.cancel.setObjectName("cancel")
        self.select_video = QtWidgets.QPushButton(VideoTransfer)
        self.select_video.setGeometry(QtCore.QRect(90, 30, 160, 32))
        self.select_video.setObjectName("select_video")
        self.select_style = QtWidgets.QPushButton(VideoTransfer)
        self.select_style.setGeometry(QtCore.QRect(350, 30, 159, 32))
        self.select_style.setObjectName("select_style")
        self.transfer = QtWidgets.QPushButton(VideoTransfer)
        self.transfer.setGeometry(QtCore.QRect(620, 30, 160, 32))
        self.transfer.setAutoDefault(False)
        self.transfer.setDefault(True)
        self.transfer.setObjectName("transfer")
        self.horizontalLayoutWidget = QtWidgets.QWidget(VideoTransfer)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 90, 786, 271))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.transfer_video = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.transfer_video.setMinimumSize(QtCore.QSize(256, 256))
        self.transfer_video.setMaximumSize(QtCore.QSize(256, 256))
        self.transfer_video.setText("")
        self.transfer_video.setObjectName("transfer_video")
        self.horizontalLayout.addWidget(self.transfer_video)
        self.style_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.style_image.setMinimumSize(QtCore.QSize(256, 256))
        self.style_image.setMaximumSize(QtCore.QSize(256, 256))
        self.style_image.setText("")
        self.style_image.setObjectName("style_image")
        self.horizontalLayout.addWidget(self.style_image)
        self.content_video = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.content_video.setMinimumSize(QtCore.QSize(256, 256))
        self.content_video.setMaximumSize(QtCore.QSize(256, 256))
        self.content_video.setText("")
        self.content_video.setObjectName("content_video")
        self.horizontalLayout.addWidget(self.content_video)

        self.retranslateUi(VideoTransfer)
        QtCore.QMetaObject.connectSlotsByName(VideoTransfer)

    def retranslateUi(self, VideoTransfer):
        _translate = QtCore.QCoreApplication.translate
        VideoTransfer.setWindowTitle(_translate("VideoTransfer", "视频风格迁移"))
        self.cancel.setText(_translate("VideoTransfer", "返回"))
        self.select_video.setText(_translate("VideoTransfer", "选择视频"))
        self.select_style.setText(_translate("VideoTransfer", "选择风格"))
        self.transfer.setText(_translate("VideoTransfer", "风格迁移"))

