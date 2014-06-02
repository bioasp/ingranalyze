# Copyright (c) 2012, Sven Thiele <sthiele78@gmail.com>
#
# This file is part of ingranalyze.
#
# ingranalyze is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ingranalyze is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ingranalyze.  If not, see <http://www.gnu.org/licenses/>.
# -*- coding: utf-8 -*-
from setuptools import setup
import os
import sys
import platform
import distutils
import site
import sysconfig

from setuptools.command.install import install as _install



class install(_install):
    def run(self):
        _install.run(self)
                         
setup(cmdclass={'install': install},
      name='ingranalyze',
      version='1.5.3',
      url='http://pypi.python.org/pypi/ingranalyze/',
      license='GPLv3+',
      description='Influence graph analysis, consistency check, diagnosis, repair and prediction.',
      long_description=open('README').read(),
      author='Sven Thiele',
      author_email='sthiele78@gmail.com',
      packages = ['__ingranalyze__'],
      package_dir = {'__ingranalyze__' : 'src'},
      package_data = {'__ingranalyze__' : ['encodings/*.lp','encodings/*.gringo']},
      scripts = ['ingranalyze.py'],
      install_requires=[
        "pyasp == 1.3.3"
      ]
)
