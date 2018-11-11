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

"""QuickQR Command Line Interface module.

Manage arguments parsing.
"""

from quickqr import QUICKQR_APPLICATION_NAME, QUICKQR_VERSION
import argparse
import logging

logger = logging.getLogger(__name__)


def parse():

    # Define the parser.
    parser=argparse.ArgumentParser(
        description="QuickQR is a Qt application that lives in your system tray. "
                    "It generate a QR code from your current clipboard data",
        formatter_class=argparse.RawDescriptionHelpFormatter,)
    parser.add_argument("--version", action="version", version="{} v{}".format(QUICKQR_APPLICATION_NAME, QUICKQR_VERSION))

    # Run the parser.
    args = parser.parse_args()

    return args