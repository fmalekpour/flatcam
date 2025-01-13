#!C:\WinPython\WPy64-31190b5\python-3.11.9.amd64\python.exe

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.pct2rgb as a convenience to use as a script
from osgeo_utils.pct2rgb import *  # noqa
from osgeo_utils.pct2rgb import main

deprecation_warn("pct2rgb")
sys.exit(main(sys.argv))
