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
        ImageTransfer.resize(901, 457)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ImageTransfer)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 70, 826, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.content_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.content_image.setMinimumSize(QtCore.QSize(256, 256))
        self.content_image.setMaximumSize(QtCore.QSize(256, 256))
        self.content_image.setText("")
        self.content_image.setObjectName("content_image")
        self.horizontalLayout.addWidget(self.content_image)
        self.style_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.style_image.setMinimumSize(QtCore.QSize(256, 256))
        self.style_image.setMaximumSize(QtCore.QSize(256, 256))
        self.style_image.setText("")
        self.style_image.setObjectName("style_image")
        self.horizontalLayout.addWidget(self.style_image)
        self.transfer_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.transfer_image.setMinimumSize(QtCore.QSize(256, 256))
        self.transfer_image.setMaximumSize(QtCore.QSize(256, 256))
        self.transfer_image.setText("")
        self.transfer_image.setObjectName("transfer_image")
        self.horizontalLayout.addWidget(self.transfer_image)
        self.cancel = QtWidgets.QPushButton(ImageTransfer)
        self.cancel.setGeometry(QtCore.QRect(400, 390, 112, 32))
        self.cancel.setAutoDefault(False)
        self.cancel.setDefault(True)
        self.cancel.setObjectName("cancel")
        self.select_content = QtWidgets.QPushButton(ImageTransfer)
        self.select_content.setGeometry(QtCore.QRect(130, 30, 100, 32))
        self.select_content.setMinimumSize(QtCore.QSize(0, 0))
        self.select_content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_content.setObjectName("select_content")
        self.select_style = QtWidgets.QPushButton(ImageTransfer)
        self.select_style.setGeometry(QtCore.QRect(400, 30, 100, 32))
        self.select_style.setMinimumSize(QtCore.QSize(0, 0))
        self.select_style.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.select_style.setObjectName("select_style")
        self.transfer = QtWidgets.QPushButton(ImageTransfer)
        self.transfer.setGeometry(QtCore.QRect(670, 30, 100, 32))
        self.transfer.setMinimumSize(QtCore.QSize(0, 0))
        self.transfer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.transfer.setAutoDefault(False)
        self.transfer.setDefault(True)
        self.transfer.setFlat(False)
        self.transfer.setObjectName("transfer")

        self.retranslateUi(ImageTransfer)
        QtCore.QMetaObject.connectSlotsByName(ImageTransfer)

    def retranslateUi(self, ImageTransfer):
        _translate = QtCore.QCoreApplication.translate
        ImageTransfer.setWindowTitle(_translate("ImageTransfer", "图像风格迁移"))
        self.cancel.setText(_translate("ImageTransfer", "返回"))
        self.select_content.setText(_translate("ImageTransfer", "选择图片内容"))
        self.select_style.setText(_translate("ImageTransfer", "选择图片风格"))
        self.transfer.setText(_translate("ImageTransfer", "风格迁移"))

