#! /usr/bin/env python
# coding: utf-8

from setuptools import find_packages, setup

setup(name='ego.io',
      author='openego development group',
      author_email='oemof@rl-institut.de',
      description='ego input/output repository',
      version='0.0.1rc3',
      url='https://github.com/openego/ego.io',
      packages=find_packages(),
      license='GNU GENERAL PUBLIC LICENSE Version 3',
      install_requires=[
          'geoalchemy2',
          "sqlalchemy[postgresql]",
          "numpy",
          "psycopg2"]
      )
