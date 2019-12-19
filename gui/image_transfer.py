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
        ImageTransfer.resize(640, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(ImageTransfer)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 30, 541, 211))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.content_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.content_image.setText("")
        self.content_image.setObjectName("content_image")
        self.verticalLayout.addWidget(self.content_image)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_7.addWidget(self.pushButton_6)
        self.style_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.style_image.setText("")
        self.style_image.setObjectName("style_image")
        self.verticalLayout_7.addWidget(self.style_image)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.transfer_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.transfer_image.setText("")
        self.transfer_image.setObjectName("transfer_image")
        self.verticalLayout_3.addWidget(self.transfer_image)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.cancel = QtWidgets.QPushButton(ImageTransfer)
        self.cancel.setGeometry(QtCore.QRect(270, 250, 112, 32))
        self.cancel.setAutoDefault(False)
        self.cancel.setDefault(True)
        self.cancel.setObjectName("cancel")

        self.retranslateUi(ImageTransfer)
        QtCore.QMetaObject.connectSlotsByName(ImageTransfer)

    def retranslateUi(self, ImageTransfer):
        _translate = QtCore.QCoreApplication.translate
        ImageTransfer.setWindowTitle(_translate("ImageTransfer", "图像风格迁移"))
        self.pushButton.setText(_translate("ImageTransfer", "选择图片内容"))
        self.pushButton_6.setText(_translate("ImageTransfer", "选择图片风格"))
        self.pushButton_2.setText(_translate("ImageTransfer", "风格迁移"))
        self.cancel.setText(_translate("ImageTransfer", "返回"))

