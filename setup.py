#! /usr/bin/env python
# coding: utf-8

from setuptools import find_packages, setup

setup(name='egoio',
      author='NEXT ENERGY, Reiner Lemoine Institut gGmbH, ZNES',
      author_email='ulf.p.mueller@hs-flensburg.de',
      description='ego input/output repository',
      version='0.4.5',
      url='https://github.com/openego/ego.io',
      packages=find_packages(),
      license='GNU Affero General Public License v3.0',
      install_requires=[
          'geoalchemy2 >= 0.3.0, <= 0.4.1',
          'sqlalchemy >= 1.0.11, <= 1.2.0',
          'keyring >= 4.0',
          'keyrings.alt',
          'psycopg2'],
      extras_require={
          "sqlalchemy": 'postgresql'},
      package_data={'tools': 'sqlacodegen_oedb.sh'}
      )
