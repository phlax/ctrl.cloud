#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python ctrl.cloud
"""

from setuptools import setup


install_requires = [
    'aiohttp',
    'ctrl.core',
    'ctrl.command']

extras_require = {}
extras_require['test'] = [
    "pytest",
    "pytest-mock",
    "coverage",
    "pytest-coverage",
    "codecov",
    "flake8"],

setup(
    name='ctrl.cloud',
    version='0.0.1',
    description='ctrl.cloud',
    long_description="ctrl.cloud",
    url='https://github.com/phlax/ctrl.cloud',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        ('License :: OSI Approved :: '
         'GNU General Public License v3 or later (GPLv3+)'),
        'Programming Language :: Python :: 3.5',
    ],
    keywords='python ctrl',
    install_requires=install_requires,
    extras_require=extras_require,
    packages=['ctrl.cloud'],
    include_package_data=True)
