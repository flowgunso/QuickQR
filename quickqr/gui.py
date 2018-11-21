# -*- coding: utf-8 -*-
#
# QuickQR, quickly generate a QR code.
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

"""QuickQR graphical module.

Is this application core.
Contains Qt bindings and QR code generation.
"""

from PyQt5.QtCore import PYQT_VERSION_STR
from quickqr import QUICKQR_HOMEPAGE_URL, QUICKQR_VERSION, QUICKQR_APPLICATION_NAME, RESOURCES_PATH

from PyQt5 import QtWidgets, QtGui
from PIL.ImageQt import ImageQt
from quickqr.ui_about import Ui_AboutWidget
from quickqr.ui_qr import Ui_QrWidget
from tempfile import NamedTemporaryFile
import qrcode
import sys
import logging

logger = logging.getLogger(__name__)


def icon(name):
    """Return a usable QtIcon using a given icon name in the application resources."""

    icons_path = RESOURCES_PATH.joinpath("icons")
    icon = icons_path.joinpath(name)
    if not icon.exists():
        raise FileExistsError
    return QtGui.QIcon(QtGui.QPixmap(str(icon)))


class MainWindow(QtWidgets.QMainWindow):
    """Application main window.

    Owns the system tray icon, the system tray icon's context menu, and contains the about widget.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(icon("quickqr.svg"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        # Instanciate as the about widget as the main window's central widget.
        self.widget_about = AboutWidget(self)
        self.setCentralWidget(self.widget_about)

        # Instanciate the tray menu.
        self.menu_system_tray = TrayMenu(self)

        # Instanciate the system tray icon with the tray menu as it's context menu.
        self.icon_system_tray = QtWidgets.QSystemTrayIcon()
        self.icon_system_tray.setIcon(icon("quickqr.svg"))
        self.icon_system_tray.setContextMenu(self.menu_system_tray)
        self.icon_system_tray.show()

        logger.debug("MainWindow have been instanciated.")

    def closeEvent(self, event):
        """Override the close event to hide the main window, not close the whole application."""
        event.ignore()
        self.hide()


class AboutWidget(QtWidgets.QWidget):
    """About widget.

    Contains information about this application.
    Allows to terminate the application.
    """

    def __init__(self, parent=None):
        super(AboutWidget, self).__init__(parent)
        self.ui = Ui_AboutWidget()
        self.ui.setupUi(self)

        # Define the about text.
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

        # Button that allow terminating the application.
        self.ui.terminate.setText("Terminate {}".format(QUICKQR_APPLICATION_NAME))
        self.ui.terminate.setIcon(icon("process-stop.svg"))
        self.ui.terminate.clicked.connect(QtWidgets.QApplication.exit)

        logger.debug("AboutWidget have been instanciated.")


class TrayMenu(QtWidgets.QMenu):
    """System tray icon's context menu.

    Contains the following actions:
    - Show/hide the about widget
    - Show the QR code.
    """

    def __init__(self, parent=None):
        super(TrayMenu, self).__init__(parent)

        # Action that show/hide the about widgect.
        self.action_show_hide_about = QtWidgets.QAction(self)
        self.action_show_hide_about.setText("About QuickQR")
        self.action_show_hide_about.triggered.connect(
            lambda: self.parent().setVisible(
                not self.parent().isVisible()
        ))
        self.addAction(self.action_show_hide_about)

        # Terminate the application.
        # self.action_terminate = QtWidgets.QAction("Terminate {}".format(QUICKQR_APPLICATION_NAME))
        # self.action_terminate.triggered.connect(QtWidgets.QApplication.exit)
        # self.addAction(self.action_terminate)

        # Separator.
        self.addSeparator()

        # The QR widget.
        self.widget_display_qr = QrWidget()

        # Action that show/hide the QR widget.
        self.action_display_qr = QtWidgets.QAction(self)
        self.action_display_qr.triggered.connect(
            lambda: self.widget_display_qr.setVisible(
                not self.widget_display_qr.isVisible()
        ))
        self.addAction(self.action_display_qr)
        # Initialise the action text.
        self.update()

        # Watch clipboard changes to update the tray menu QR displaying action text.
        QtWidgets.QApplication.clipboard().dataChanged.connect(self.update)

        logger.debug("TrayMenu have been instanciated.")


    def update(self):
        """Update the action's text that displays the QR code depending on the clipboard."""

        clipboard = QtWidgets.QApplication.clipboard().text()
        if clipboard:
            if sys.getsizeof(clipboard) <= 4096:
                text = "QR of current clipboard"
                enabled = True
            else:
                text = "Current clipboard is too large (>4kB) to generate a QR code!"
                enabled = False
        else:
            text = "Current clipboard is empty..."
            enabled = False
        self.action_display_qr.setText(text)
        self.action_display_qr.setEnabled(enabled)

        logger.debug("QR action's text have changed.")


class QrWidget(QtWidgets.QWidget):
    """Widget that display the QR code generated.

    This is the main feature of this application.
    When the clipboard changes, a new QR code is generated and written to disk.
    """

    def __init__(self, parent=None):
        super(QrWidget, self).__init__(parent)
        self.ui = Ui_QrWidget()
        self.ui.setupUi(self)
        self.setWindowIcon(icon("quickqr.svg"))

        # Define the initial QR image file state.
        # self.temporary_qr_image_file = None
        self.update()

        # Watch for clipboard changes to update the QR code.
        QtWidgets.QApplication.clipboard().dataChanged.connect(self.update)

        logger.debug("QrWidget have been instanciated.")


    def update(self):
        """Update the QR widget content by generate a new QR image file.

        Is trigger on clipboard changes, therefore QR code will be different that the previously generated.
        """

        clipboard = QtWidgets.QApplication.clipboard().text()

        # Prevent crashes when generating empty or oversized QR codes.
        if clipboard:
            if sys.getsizeof(clipboard) <= 4096:

                # # Close the last temporary QR image file.
                # if self.temporary_qr_image_file is not None:
                #     self.temporary_qr_image_file.close()

                # Generate QR code and save it to the temporary file.

                qr = ImageQt(qrcode.make(clipboard))

                # Set the text displayed in the widget as HTML.
                self.ui.label_qr.setPixmap(QtGui.QPixmap.fromImage(qr))
                self.ui.label_clipboard.setText(clipboard)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
