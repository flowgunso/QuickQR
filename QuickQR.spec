# -*- mode: python -*-

import platform

block_cipher = None

runtime_system = platform.system()
if runtime_system == "Linux":
    executable_name = 'QuickQR_linux'
elif runtime_system == "Darwin":
    executable_name = 'QuickQR_osx'
else:
    executable_name = "QuickQR"

a = Analysis(['entrypoint.py'],
             pathex=['/home/florian/Workspaces/applications/Jetbrains/PyCharm/QuickQR'],
             binaries=[],
             datas=[('resources/icons', 'resources/icons')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name=executable_name,
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          icon='resources/icons/quickqr.ico',
          console=False
          )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='QuickQR')

if platform.system() == 'Darwin':
    app = BUNDLE(coll,
                 name='QuickQR.app',
                 icon='resources/icons/quickqr.icns',
                 bundle_identifier=None,
                 )
