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

from PyQt5.QtWidgets import QApplication
from quickqr import ROOT_PATH, QUICKQR_APPLICATION_NAME
from quickqr import gui, cli
import logging
import sys


def entrypoint():
    """QuickQR application entrypoint.

    Used with PyInstaller for it's entrypoint.
    Also use it to run from source.
    """
    # Define loggers.
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # Define handlers.
    file_handler = logging.FileHandler(str(ROOT_PATH.joinpath("{}.log".format(QUICKQR_APPLICATION_NAME))))
    console_handler = logging.StreamHandler()
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    console_handler.setFormatter(logging.Formatter('%(message)s'))
    # Set handlers to loggers.
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.debug("Parsing given arguments")
    args = cli.parse()

    logger.debug("QuickQR is starting...")
    app = QApplication(sys.argv)
    mw = gui.MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    entrypoint()