#! /usr/bin/env python
# coding: utf-8

from setuptools import find_packages, setup

setup(name='egoio',
      author='openego development group',
      author_email='oemof@rl-institut.de',
      description='ego input/output repository',
      version='0.0.2',
      url='https://github.com/openego/ego.io',
      packages=find_packages(),
      license='GNU GENERAL PUBLIC LICENSE Version 3',
      install_requires=[
          'geoalchemy2 >= 0.3.0, <=0.3.0',
          'sqlalchemy >= 1.0.15, <= 1.1.4',
          "numpy >= 1.11.2, <= 1.11.2"],
      extras_require={
          "sqlalchemy": 'postgresql'}
      )
