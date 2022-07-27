# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/Michael/PycharmProjects/CookieClicker/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/Michael/PycharmProjects/CookieClicker/cookie.py', '.'), ('C:/Users/Michael/PycharmProjects/CookieClicker/cookieDisplay.py', '.'), ('C:/Users/Michael/PycharmProjects/CookieClicker/cookieHandler.py', '.'), ('C:/Users/Michael/PycharmProjects/CookieClicker/cookieParticle.py', '.'), ('C:/Users/Michael/PycharmProjects/CookieClicker/goldenCookie.py', '.'), ('C:/Users/Michael/PycharmProjects/CookieClicker/utils.py', '.'), ('C:/Users/Michael/PycharmProjects/CookieClicker/textures', 'textures/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
splash = Splash(
    'C:/Users/Michael/PycharmProjects/CookieClicker/textures/icon/splash.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='CookieClicker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Users\\Michael\\PycharmProjects\\CookieClicker\\textures\\icon\\icon.ico',
)
