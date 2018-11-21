$client = new-object System.Net.WebClient
$client.DownloadFile("https://imagemagick.org/download/binaries/ImageMagick-7.0.8-14-Q16-x64-static.exe","ImageMagick.exe")

ImageMagick.exe convert resources/icons/quickqr.svg -bordercolor white -border 0 |
          -clone 0 -resize 16x16 -clone 0 -resize 32x32 -clone 0 -resize 48x48 |
          -clone 0 -resize 64x64 -clone 0 -resize 128x128 |
          -clone 0 -resize 256x256 -clone 0 -resize 512x512 |
          -colors 256 resources/icons/quickqr.ico

Import-Module %PYTHON%
%PYTHON%\python.exe -m pip install -r requirements.txt
%PYTHON%\python.exe -m pip install -r scripts/requirements.txt