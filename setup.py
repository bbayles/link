#!/usr/bin/env python
from setuptools import setup

VERSION = (0, 0, 4)
NAME = 'link'
DESCRIPTION = "Easy and consistent access to the objects you care about"
LONG_DESCRIPTION = "Easy and consistent access to the objects you care about"
URL = ''
LICENSE = 'MIT'
DOWNLOAD_URL = ''
CLASSIFIERS = ['Development Status :: 4 - Beta',     
               'Programming Language :: Python',
               'Programming Language :: Python :: 2'
              ]
AUTHOR = ''
EMAIL = ''
VERSION_STRING = '.'.join(map(str,VERSION))
SETUP_ARGS = {}
DATA_FILES = [('link/configs', ['link/configs/link.config'])]
REQUIRES = ['pandas >= 0.6.0', 'numpy >= 1.6.0',
            'requests >=0.11', 'MySQL-python'] 

def write_version(filename='link/version.py'):
    """
    Write out the version python file to the link directory before installing
    """
    cnt = "version = '%s'\nversion_details = %s\n"
    a = open(filename, 'w')
    try:
        a.write(cnt % (VERSION_STRING, VERSION))
    finally:
        a.close()

# write out the version file so we can keep track on what version the built
# package is
write_version()

# call setup so it can build the package
setup(name=NAME,
      version=VERSION_STRING,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      license=LICENSE,
      maintainer_email=EMAIL,
      maintainer=AUTHOR,
      url=URL,
      packages=['link', 'link.wrappers', 'link.configs'],
      #package_data = {'link.configs': ['link.configs/*config']},
      install_requires = REQUIRES,
      data_files = DATA_FILES,
      classifiers=CLASSIFIERS,
      **SETUP_ARGS)
