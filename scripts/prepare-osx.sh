#!/bin/bash

# Install Python on OSX.
wget "https://www.python.org/ftp/python/3.6.6/python-3.6.6-macosx10.9.pkg"
sudo installer -pkg python-3.6.6-macosx10.9.pkg -target /
sudo python3 -m ensurepip
pip3 install --upgrade pip setuptools wheel
pip3 install virtualenv
python3 -m virtualenv -p python3 .
source bin/activate