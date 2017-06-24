#!/usr/bin/env python

from setuptools import setup

setup(name='django-notifs',
      version='1.2',
      description='Re-usable notification app for Django',
      url='https://github.com/danidee10/django-notifs',
      author='Osaetin Daniel',
      author_email='osaetindaniel@gmail.com',
      license='GPL',
      packages=['notifications'],
      install_requires=[
          'django',
      ],
      zip_safe=False)
