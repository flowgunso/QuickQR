# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qr.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QrWidget(object):
    def setupUi(self, QrWidget):
        QrWidget.setObjectName("QrWidget")
        QrWidget.resize(190, 72)
        self.verticalLayout = QtWidgets.QVBoxLayout(QrWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(QrWidget)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(QrWidget)
        QtCore.QMetaObject.connectSlotsByName(QrWidget)

    def retranslateUi(self, QrWidget):
        _translate = QtCore.QCoreApplication.translate
        QrWidget.setWindowTitle(_translate("QrWidget", "QuickQR - Code"))

