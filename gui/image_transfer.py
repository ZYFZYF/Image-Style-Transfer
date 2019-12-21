# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_transfer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageTransfer(object):
    def setupUi(self, ImageTransfer):
        ImageTransfer.setObjectName("ImageTransfer")
        ImageTransfer.resize(901, 453)
        self.cancel = QtWidgets.QPushButton(ImageTransfer)
        self.cancel.setGeometry(QtCore.QRect(310, 390, 112, 32))
        self.cancel.setAutoDefault(False)
        self.cancel.setDefault(True)
        self.cancel.setObjectName("cancel")
        self.select_content = QtWidgets.QPushButton(ImageTransfer)
        self.select_content.setGeometry(QtCore.QRect(110, 30, 131, 32))
        self.select_content.setMinimumSize(QtCore.QSize(0, 0))
        self.select_content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_content.setObjectName("select_content")
        self.select_style = QtWidgets.QPushButton(ImageTransfer)
        self.select_style.setGeometry(QtCore.QRect(380, 30, 131, 32))
        self.select_style.setMinimumSize(QtCore.QSize(0, 0))
        self.select_style.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_style.setObjectName("select_style")
        self.select_algorithm = QtWidgets.QPushButton(ImageTransfer)
        self.select_algorithm.setGeometry(QtCore.QRect(650, 30, 131, 32))
        self.select_algorithm.setMinimumSize(QtCore.QSize(0, 0))
        self.select_algorithm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_algorithm.setAutoDefault(True)
        self.select_algorithm.setDefault(False)
        self.select_algorithm.setFlat(False)
        self.select_algorithm.setObjectName("select_algorithm")
        self.start = QtWidgets.QPushButton(ImageTransfer)
        self.start.setGeometry(QtCore.QRect(480, 390, 112, 32))
        self.start.setDefault(True)
        self.start.setObjectName("start")
        self.content_image = QtWidgets.QLabel(ImageTransfer)
        self.content_image.setGeometry(QtCore.QRect(50, 90, 256, 256))
        self.content_image.setMinimumSize(QtCore.QSize(256, 256))
        self.content_image.setMaximumSize(QtCore.QSize(256, 256))
        self.content_image.setText("")
        self.content_image.setObjectName("content_image")
        self.style_image = QtWidgets.QLabel(ImageTransfer)
        self.style_image.setGeometry(QtCore.QRect(320, 90, 256, 256))
        self.style_image.setMinimumSize(QtCore.QSize(256, 256))
        self.style_image.setMaximumSize(QtCore.QSize(256, 256))
        self.style_image.setText("")
        self.style_image.setObjectName("style_image")
        self.transfer_image = QtWidgets.QLabel(ImageTransfer)
        self.transfer_image.setGeometry(QtCore.QRect(590, 90, 256, 256))
        self.transfer_image.setMinimumSize(QtCore.QSize(256, 256))
        self.transfer_image.setMaximumSize(QtCore.QSize(256, 256))
        self.transfer_image.setText("")
        self.transfer_image.setObjectName("transfer_image")

        self.retranslateUi(ImageTransfer)
        QtCore.QMetaObject.connectSlotsByName(ImageTransfer)

    def retranslateUi(self, ImageTransfer):
        _translate = QtCore.QCoreApplication.translate
        ImageTransfer.setWindowTitle(_translate("ImageTransfer", "图像风格迁移"))
        self.cancel.setText(_translate("ImageTransfer", "返回"))
        self.select_content.setText(_translate("ImageTransfer", "选择图片内容"))
        self.select_style.setText(_translate("ImageTransfer", "选择图片风格"))
        self.select_algorithm.setText(_translate("ImageTransfer", "选择算法"))
        self.start.setText(_translate("ImageTransfer", "迁移"))

