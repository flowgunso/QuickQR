#!/bin/bash

# Build the OSX icns.
resources_path="resources"
svg_path="${resources_path}/icons/quickqr.svg"
iconset_path="${resources_path}/iconset"
icns_path="${resources_path}/icons/quickqr.icns"
mkdir "${iconset_path}"
sips -z 16 16  "${svg_path}" --out "${iconset_path}/icon_16x16.png"
sips -z 32 32  "${svg_path}" --out "${iconset_path}/icon_16x16@2x.png"
sips -z 32 32  "${svg_path}" --out "${iconset_path}/icon_32x32.png"
sips -z 25 25 "${svg_path}" --out "${iconset_path}/icon_25x25@2x.png"
sips -z 64 64  "${svg_path}" --out "${iconset_path}/icon_32x32@2x.png"
sips -z 128 128  "${svg_path}" --out "${iconset_path}/icon_128x128.png"
sips -z 256 256  "${svg_path}" --out "${iconset_path}/icon_128x128@2x.png"
sips -z 256 256  "${svg_path}" --out "${iconset_path}/icon_256x256.png"
sips -z 512 512  "${svg_path}" --out "${iconset_path}/icon_256x256@2x.png"
sips -z 512 512  "${svg_path}" --out "${iconset_path}/icon_512x512.png"
sips -z 1024 1024  "${svg_path}" --out "${iconset_path}/icon_512x512@2x.png"
iconutil -c icns "${iconset_path}" -o

# Install Python on OSX.
wget "https://www.python.org/ftp/python/3.6.6/python-3.6.6-macosx10.9.pkg"
sudo installer -pkg python-3.6.6-macosx10.9.pkg -target /
sudo python3 -m ensurepip
pip3 install --upgrade pip setuptools wheel
pip3 install virtualenv
python3 -m virtualenv -p python3 .
source bin/activate

