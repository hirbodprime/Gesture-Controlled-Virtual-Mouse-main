# -*- mode: python ; coding: utf-8 -*-
def get_mediapipe_path():
    import mediapipe
    mediapipe_path = mediapipe.__path__[0]
    return mediapipe_path

block_cipher = None

a = Analysis(['src\\Gesture_Controller.py'],
             pathex=[],
             binaries=[],
             datas=[
                 ('demo_media', 'demo_media'),
                 ('src\\calib_images', 'calib_images'),
                 ('src\\web', 'web'),
             ],
             hiddenimports=[
                 'opencv-python',
                 'mediapipe',
                 'pyautogui',
                 'pillow',
                 'enum',
                 'mediapipe.solutions',
                 'ctypes',
                 'comtypes',
                 'pycaw.pycaw',
                 'google.protobuf.json_format',
                 'screen_brightness_control',
                 'numpy',
                 'glob',
                 'pyttsx3',
                 'speech_recognition',
                 'webbrowser',
                 'datetime',
                 'pynput.keyboard',
                 'smtplib',
                 'wikipedia',
             ],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             noarchive=False,
             )

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
mediapipe_tree = Tree(get_mediapipe_path(), prefix='mediapipe', excludes=["*.pyc"])
a.datas += mediapipe_tree
a.binaries = filter(lambda x: 'mediapipe' not in x[0], a.binaries)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Gesture_Controller',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon=None,
          disable_windowed_traceback=False,
          argv_emulation=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Gesture_Controller')
