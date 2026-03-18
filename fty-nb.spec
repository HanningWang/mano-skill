# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['visual/vla.py'],
    pathex=['.'],
    binaries=[],
    datas=[],
    hiddenimports=[
        'visual',
        'visual.config.visual_config',
        'visual.model.task_model',
        'visual.model.task_progress',
        'visual.model.task_state',
        'visual.view.task_overlay_view',
        'visual.view_model.task_view_model',
        'visual.computer.computer_action_executor',
        'visual.computer.computer_use_util',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='fty-nb',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
