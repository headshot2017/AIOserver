import urllib2
import zipfile
import subprocess
import sys
import os

def pip_install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

print "installing iniconfig"
pip_install('iniconfig')

print "installing pyinstaller"
pip_install('pyinstaller')

print "done"
