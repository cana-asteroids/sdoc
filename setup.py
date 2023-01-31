#!/usr/bin/env python

from setuptools import setup

# PACKAGE METADATA
# ##################
NAME = 'cana-sdoc'
FULLNAME = "SDOC"
VERSION = '0.131'
DESCRIPTION = 'Small Database of Optical Constants'
with open("README.rst") as f:
    LONG_DESCRIPTION = ''.join(f.readlines())
AUTHOR = '''M. De Pra'''
AUTHOR_EMAIL = 'mariondepra@gmail.com'
MAINTAINER = 'M. De Pra'
MAINTAINER_EMAIL = AUTHOR_EMAIL
URL = 'https://github.com/depra/sdoc'
LICENSE = 'MIT License'

# TO BE INSTALLED
# ##################
PACKAGES = ['sdoc']

PACKAGE_DATA = {
   'sdoc': ['data/*', 'data/oc_files/*/*']
}

# DEPENDENCIES
# ##################
INSTALL_REQUIRES = [
    'numpy>=1.21',
    'pandas',
    'h5py',
]

PYTHON_REQUIRES = ">=3.6"

if __name__ == '__main__':
    setup(name=NAME,
          description=DESCRIPTION,
          #   long_description=LONG_DESCRIPTION,
          version=VERSION,
          author=AUTHOR,
          author_email=AUTHOR_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          license=LICENSE,
          url=URL,
          #   platforms=PLATFORMS,
          #   scripts=SCRIPTS,
          packages=PACKAGES,
          #   ext_modules=EXT_MODULES,
          package_data=PACKAGE_DATA,
          #   classifiers=CLASSIFIERS,
          #   keywords=KEYWORDS,
          #   cmdclass=CMDCLASS,
          install_requires=INSTALL_REQUIRES,
          python_requires=PYTHON_REQUIRES,
          )
