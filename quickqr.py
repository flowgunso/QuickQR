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

from PyQt5.QtWidgets import QApplication
from quickqr import gui
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = gui.MainWindow()
    sys.exit(app.exec())