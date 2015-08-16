#!/usr/bin/env python
from setuptools import setup
from setuptools import find_packages

setup(
    name='cbng_interface',
    version='1.0.0',
    description='ClueBot NG Interface',
    author='Damian Zaremba',
    author_email='damian@damianzaremba.co.uk',
    packages=find_packages(exclude=['tests*']),
    setup_requires=['nose', 'flake8', 'coverage'],
    install_requires=[],
)
