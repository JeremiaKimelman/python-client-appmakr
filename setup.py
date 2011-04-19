#!/usr/bin/env python
from setuptools import setup, find_packages
import os, re

PKG='appmakr'
VERSIONFILE = os.path.join('appmakr', '_version.py')
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    MVSRE = r"^manual_verstr *= *['\"]([^'\"]*)['\"]"
    mo = re.search(MVSRE, verstrline, re.M)
    if mo:
        mverstr = mo.group(1)
    else:
        print "unable to find version in %s" % (VERSIONFILE,)
        raise RuntimeError("if %s.py exists, it must be well-formed" % (VERSIONFILE,))
    AVSRE = r"^auto_build_num *= *['\"]([^'\"]*)['\"]"
    mo = re.search(AVSRE, verstrline, re.M)
    if mo:
        averstr = mo.group(1)
    else:
        averstr = ''
    verstr = '.'.join([mverstr, averstr])

setup_requires = []
tests_require = ['mock']

setup(name=PKG,
      version=verstr,
      description="Library for interfacing with Appmakrs API",
      author="Dan Patey & Isaac Mosquera",
      author_email="Dan.Patey@Appmakr.com",
      url="http://github.com/Appmakr/python-appmakr",
      packages = find_packages(),
      license = "MIT License",
      install_requires=['httplib2>=0.6.0', 'oauth2>=1.5', 'pyutil[jsonutil] >= 1.8.1', 'ipaddr >= 2.0.0'],
      keywords="appmakr",
      zip_safe=False, # actually it is zip safe, but zipping packages doesn't help with anything and can cause some problems (http://bugs.python.org/setuptools/issue33 )
      test_suite='appmakr.test',
      setup_requires=setup_requires,
      tests_require=tests_require)
