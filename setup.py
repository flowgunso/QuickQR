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
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from setuptools import Command, setup, find_packages
from quickqr import QUICKQR_ORGANISATION_NAME, QUICKQR_APPLICATION_NAME, QUICKQR_VERSION
import os
from pathlib import Path
import glob

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class build_ui(Command):
    """Build files issued from Qt Designer into Python.
    """

    description = "Build files issued from Qt Designer into Python."
    user_options = [
        ("files=", None, "colon-separated list of files to build."),
    ]

    def initialize_options(self):
        self.files = None

    def finalize_options(self):
        files = []
        if self.files:
            for file in self.files.split(':'):
                path = Path(file)
                if not path.is_file():
                    print("{} is not a file.".format(path))
                    continue
                files.append(path)
        else:
            tmp = glob.glob("{}/resource/ui/*.ui".format(ROOT_PATH))
            for file in tmp:
                path = Path(file)
                files.append(path)
        self.files = files

    def run(self):
        from PyQt5 import QtWidgets, uic
        # import sys
        # app = QtWidgets.QApplication(sys.argv)

        for file in self.files:
            pyui_filename = "ui_{}.py".format(file.stem)
            destination = Path(ROOT_PATH).joinpath("quickqr", pyui_filename)

            with open(destination, 'w') as o:
                uic.compileUi(file, o)
                # w = uic.loadUi(file)
                # w.show()

        # sys.exit(app.exec_())

with open('README.md', mode='r', encoding='utf-8') as f:
    long_description = f.read()

args = {
    'name': QUICKQR_APPLICATION_NAME.lower(),
    'version': QUICKQR_VERSION,
    'description': 'QuickQR, quickly generate a QR code.',
    'keywords': 'system tray systemtray qr qrcode',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'packages': find_packages(),
    'cmdclass': {
        'build_ui': build_ui,
    },
    'install_requires': ['PyQt5'],
    'classifiers': [
        'Development Status:: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
}

setup(**args)
