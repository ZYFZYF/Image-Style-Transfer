# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_algorithm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectAlgorithm(object):
    def setupUi(self, SelectAlgorithm):
        SelectAlgorithm.setObjectName("SelectAlgorithm")
        SelectAlgorithm.resize(400, 216)
        self.verticalLayoutWidget = QtWidgets.QWidget(SelectAlgorithm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 40, 271, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Gatys = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Gatys.setChecked(True)
        self.Gatys.setObjectName("Gatys")
        self.verticalLayout.addWidget(self.Gatys)
        self.Chen = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Chen.setObjectName("Chen")
        self.verticalLayout.addWidget(self.Chen)
        self.Johnson = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.Johnson.setObjectName("Johnson")
        self.verticalLayout.addWidget(self.Johnson)
        self.horizontalLayoutWidget = QtWidgets.QWidget(SelectAlgorithm)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 130, 226, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.start = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start.setDefault(True)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)

        self.retranslateUi(SelectAlgorithm)
        QtCore.QMetaObject.connectSlotsByName(SelectAlgorithm)

    def retranslateUi(self, SelectAlgorithm):
        _translate = QtCore.QCoreApplication.translate
        SelectAlgorithm.setWindowTitle(_translate("SelectAlgorithm", "选择使用的算法"))
        self.Gatys.setText(_translate("SelectAlgorithm", "Gatys(最慢，~4min)"))
        self.Chen.setText(_translate("SelectAlgorithm", "Chen(较快，~1s）"))
        self.Johnson.setText(_translate("SelectAlgorithm", "Johnson(最快，~100ms，但style有限制）"))
        self.cancel.setText(_translate("SelectAlgorithm", "返回"))
        self.start.setText(_translate("SelectAlgorithm", "开始生成"))

