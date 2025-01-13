#!C:\WinPython\WPy64-31190b5\python-3.11.9.amd64\python.exe

import sys

from osgeo.gdal import deprecation_warn

# import osgeo_utils.gdalcompare as a convenience to use as a script
from osgeo_utils.gdalcompare import *  # noqa
from osgeo_utils.gdalcompare import main

deprecation_warn("gdalcompare")
sys.exit(main(sys.argv))
