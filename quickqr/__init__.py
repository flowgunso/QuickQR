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

import sys
import os
from pathlib import Path

QUICKQR_ORGANISATION_NAME="flow.gunso@gmail.com"
QUICKQR_APPLICATION_NAME="QuickQR"
QUICKQR_HOMEPAGE_URL = "http://gitlab.com/flowgunso/QuickQR"
QUICKQR_VERSION = "0.dev0"
ROOT_PATH = Path(os.path.dirname(os.path.abspath(sys.argv[0])))

if getattr(sys, 'frozen', False):
    RUNTIME_PATH = Path(sys._MEIPASS)
else:
    RUNTIME_PATH = ROOT_PATH

RESOURCES_PATH = RUNTIME_PATH.joinpath('resources')