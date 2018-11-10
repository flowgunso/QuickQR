# -*- coding: utf-8 -*-
#
# QuickQR, get QR code using your clipboard from your system tray.
# Copyright (C) 2018 flow.gunso@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from PyQt5.QtCore import PYQT_VERSION_STR
from quickqr import QUICKQR_HOMEPAGE_URL, QUICKQR_VERSION, QUICKQR_APPLICATION_NAME

from PyQt5 import QtWidgets, QtGui
from quickqr.ui_about import Ui_AboutWidget
from quickqr.ui_qr import Ui_QrWidget
from pathlib import Path
from tempfile import NamedTemporaryFile
import qrcode
import sys


def icon(name):
    resource_path = Path(__file__).parent.parent.joinpath("resource")
    icons_path = resource_path.joinpath("icons")
    icon = icons_path.joinpath(name)
    if not icon.exists():
        raise FileExistsError
    return QtGui.QIcon(QtGui.QPixmap(str(icon)))


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(icon("quickqr.svg"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.widget_about = AboutWidget(self)
        self.setCentralWidget(self.widget_about)

        self.menu_system_tray = TrayMenu(self)

        self.icon_system_tray = QtWidgets.QSystemTrayIcon()
        self.icon_system_tray.setIcon(icon("quickqr.svg"))
        self.icon_system_tray.setContextMenu(self.menu_system_tray)
        self.icon_system_tray.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def showEvent(self, event):
        self.menu_system_tray.action_show_hide_about.update()

    def hideEvent(self, event):
        self.menu_system_tray.action_show_hide_about.update()


class AboutWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(AboutWidget, self).__init__(parent)
        self.ui = Ui_AboutWidget()
        self.ui.setupUi(self)

        text = """
        <div align="center">
            <p style="font-size: xx-large"><strong>QuickQR</strong><br>v{}</p>
            <p style="font-size: large">Generate a QR code from your clipboard</p>
            <p style="font-size: medium">Documentation, upcoming features, bug reports<br>
                <a href="{}">{}</a></p>
            <p style="font-size: small">
                <u>Run with</u><br>
                Python v3.6, PyQt v{}, qrcode v6.0
            </p>
        </div>""".format(QUICKQR_VERSION, QUICKQR_HOMEPAGE_URL, QUICKQR_HOMEPAGE_URL, PYQT_VERSION_STR)
        self.ui.about.setText(text)

        # self.ui.close.setText("Close")
        self.ui.terminate.setText("Terminate {}".format(QUICKQR_APPLICATION_NAME))
        self.ui.terminate.setIcon(icon("process-stop.svg"))
        self.ui.terminate.clicked.connect(QtWidgets.QApplication.exit)


class TrayMenu(QtWidgets.QMenu):

    def __init__(self, parent=None):
        super(TrayMenu, self).__init__(parent)
        # Show/hide the about.
        self.action_show_hide_about = ShowHideAction(parent)
        self.addAction(self.action_show_hide_about)
        # Terminate the application.
        # self.action_terminate = QtWidgets.QAction("Terminate {}".format(QUICKQR_APPLICATION_NAME))
        # self.action_terminate.triggered.connect(QtWidgets.QApplication.exit)
        # self.addAction(self.action_terminate)
        # Separator.
        self.addSeparator()
        # The QR displaying!
        self.action_display_qr = QtWidgets.QAction(self)
        self.widget_display_qr = QrWidget()
        self.action_display_qr.triggered.connect(self.widget_display_qr.show)
        self.addAction(self.action_display_qr)

        self.update()

        QtWidgets.QApplication.clipboard().dataChanged.connect(self.update)


    def update(self):
        clipboard = QtWidgets.QApplication.clipboard().text()
        if clipboard:
            if sys.getsizeof(clipboard) <= 4096:
                text = "Show QR of current clipboard"
                enabled = True
            else:
                text = "Current clipboard is too large (>4kB) to generate a QR code!"
                enabled = False
        else:
            text = "Current clipboard is empty..."
            enabled = False

        self.action_display_qr.setText(text)
        self.action_display_qr.setEnabled(enabled)


class QrWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(QrWidget, self).__init__(parent)
        self.ui = Ui_QrWidget()
        self.ui.setupUi(self)
        self.setWindowIcon(icon("quickqr.svg"))
        self.temporary_file = None
        self.update()

        QtWidgets.QApplication.clipboard().dataChanged.connect(self.update)


    def update(self):
        clipboard = QtWidgets.QApplication.clipboard().text()
        if self.temporary_file is not None:
            self.temporary_file.close()

        if clipboard:
            if sys.getsizeof(clipboard) <= 4096:
                # Generate QR code and save it to the temporary file.
                qr = qrcode.make(clipboard)
                self.temporary_file = NamedTemporaryFile(mode="wb")
                qr.save(self.temporary_file)

                # Set the text displayed in the widget as HTML.
                text = """
                    <div align="center">
                        <img src="{}" width="500" height="500"/><br>
                        {}
                    </div>""".format(self.temporary_file.name, clipboard)
                self.ui.label.setText(text)
                return
        self.hide()


    def closeEvent(self, event):
        event.ignore()
        self.temporary_file.close()
        self.temporary_file = None
        self.destroy()


class ShowHideAction(QtWidgets.QAction):
    def __init__(self, parent=None):
        super(ShowHideAction, self).__init__(parent)
        self.update()

    def update(self):
        if self.parent().isVisible():
            self.setText("Hide about")
            self.triggered.connect(self.parent().hide)
        else:
            self.setText("Show about")
            self.triggered.connect(self.parent().show)