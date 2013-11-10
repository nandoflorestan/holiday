#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://peak.telecommunity.com/DevCenter/setuptools#developer-s-guide
# from distutils.core import setup
from setuptools import setup, find_packages
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

dependencies = ['nine', 'python-dateutil']
# from sys import version
# if version.startswith('2.6'):
#     dependencies.append('ordereddict')

setup(
    url='https://github.com/nandoflorestan/holiday',
    name="holiday",
    author='Nando Florestan',
    version='0.0.2dev',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    author_email="nandoflorestan@gmail.com",
    description="Information about holiday dates in many nations",
    long_description=long_description,
    zip_safe=False,
    # test_suite='holiday.tests',
    install_requires=dependencies,
    keywords=['holiday', 'holidays', 'work day', 'work days', 'working days',
              'business day', 'business days'],
    classifiers=[  # http://pypi.python.org/pypi?:action=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        'Programming Language :: Python :: Implementation :: CPython',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
