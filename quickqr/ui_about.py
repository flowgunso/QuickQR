# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutWidget(object):
    def setupUi(self, AboutWidget):
        AboutWidget.setObjectName("AboutWidget")
        AboutWidget.resize(160, 86)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.about = QtWidgets.QLabel(AboutWidget)
        self.about.setText("")
        self.about.setAlignment(QtCore.Qt.AlignCenter)
        self.about.setWordWrap(True)
        self.about.setOpenExternalLinks(True)
        self.about.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.about.setObjectName("about")
        self.verticalLayout.addWidget(self.about)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.layout_buttons = QtWidgets.QHBoxLayout()
        self.layout_buttons.setObjectName("layout_buttons")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_buttons.addItem(spacerItem1)
        self.terminate = QtWidgets.QPushButton(AboutWidget)
        self.terminate.setText("")
        self.terminate.setObjectName("terminate")
        self.layout_buttons.addWidget(self.terminate)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_buttons.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.layout_buttons)

        self.retranslateUi(AboutWidget)
        QtCore.QMetaObject.connectSlotsByName(AboutWidget)

    def retranslateUi(self, AboutWidget):
        _translate = QtCore.QCoreApplication.translate
        AboutWidget.setWindowTitle(_translate("AboutWidget", "QuickQR - About"))

