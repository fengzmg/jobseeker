#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='jobseeker',
    version='0.1.0',
    description='Python App for Job Seekers',
    long_description=readme + '\n\n' + history,
    author='Meng Feng',
    author_email='mengfeng0904@gmail.com',
    url='https://github.com/mengfeng/jobseeker',
    packages=[
        'jobseeker',
    ],
    package_dir={'jobseeker': 'jobseeker'},
    include_package_data=True,
    install_requires=[
        'pyquery', 'requests', 'pytest'
    ],
    license="BSD",
    zip_safe=False,
    keywords='jobseeker',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
)
