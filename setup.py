from setuptools import find_packages, setup

try:
    from pyqt_distutils.build_ui import build_ui
    cmdclass = {"build_ui": build_ui}
except ImportError:
    cmdclass = {}

setup(
    name="Plover: WPM and strokes meter",
    version="0.1",
    description="A meter to show your typing speed in Plover.",
    author="Waleed Khan",
    author_email="me@waleedkhan.name",
    license="GPLv3",
    install_requires=[
        "plover>=4.0.0.dev0",
        "textstat>=0.3.1",
    ],
    packages=find_packages(),
    entry_points="""
    [plover.gui.qt.tool]
    wpm_meter = plover_wpm_meter:PloverWpmMeter
    strokes_meter = plover_wpm_meter:PloverStrokesMeter
    """,
    cmdclass=cmdclass,
)
