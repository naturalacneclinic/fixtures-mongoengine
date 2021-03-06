#!/usr/bin/env python
from setuptools import setup

setup(name='fixtures_mongoengine',
      version='1.3.1',
      description='MongoEngine Fixtures.',
      author='Vitaly Nikitin',
      author_email='alaris.nik@gmail.com',
      url='https://github.com/coderfly/fixtures-mongoengine/',
      install_requires=['mongoengine>=0.8.6', 'six'],
      packages=['fixtures_mongoengine'],
      keywords=['testing', 'fixtures', 'mongoengine']
      )
