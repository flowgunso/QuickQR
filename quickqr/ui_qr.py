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
        QrWidget.resize(94, 58)
        self.verticalLayout = QtWidgets.QVBoxLayout(QrWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_qr = QtWidgets.QLabel(QrWidget)
        self.label_qr.setText("")
        self.label_qr.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qr.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_qr.setObjectName("label_qr")
        self.verticalLayout.addWidget(self.label_qr)
        self.label_clipboard = QtWidgets.QLabel(QrWidget)
        self.label_clipboard.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_clipboard.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_clipboard.setText("")
        self.label_clipboard.setTextFormat(QtCore.Qt.RichText)
        self.label_clipboard.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clipboard.setWordWrap(True)
        self.label_clipboard.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_clipboard.setObjectName("label_clipboard")
        self.verticalLayout.addWidget(self.label_clipboard)

        self.retranslateUi(QrWidget)
        QtCore.QMetaObject.connectSlotsByName(QrWidget)

    def retranslateUi(self, QrWidget):
        _translate = QtCore.QCoreApplication.translate
        QrWidget.setWindowTitle(_translate("QrWidget", "QuickQR - Code"))

