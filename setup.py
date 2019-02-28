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

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name             = 'ingranalyze',
  version          = '1.5.6',
  url              = 'http://bioasp.github.io/ingranalyze/',
  license          = 'GPLv3+',
  description      = 'Influence graph analysis, consistency check, diagnosis, repair and prediction.',
  long_description = long_description,
  long_description_content_type="text/markdown",
  author           = 'Sven Thiele',
  author_email     = 'sthiele78@gmail.com',
  packages         = ['__ingranalyze__'],
  package_dir      = {'__ingranalyze__' : 'src'},
  package_data     = {'__ingranalyze__' : ['encodings/*.lp','encodings/*.gringo']},
  scripts          = ['ingranalyze.py'],
  install_requires = ['pyasp == 1.4.4']
)
