#!/usr/bin/python

import os
from setuptools import setup

DESCRIPTION = "dictools"

README = os.path.join(os.path.dirname(__file__), 'README.rst')

try:
    with open(README) as README_file:
        long_description = README_file.read()
except EnvironmentError:
    long_description = ''

setup(
    name="dictools",
    version="0.1",
    description=DESCRIPTION,
    long_description=long_description,
    license="MIT License",
    author="Evgeny Bogodukhov",
    author_email="boevgeny@gmail.com",
    maintainer="Evgeny Bogodukhov",
    maintainer_email="boevgeny@gmail.com",
    url="https://github.com/boevgeny/dictools",
    platforms=["any"],
    packages=[
        "dictools",
    ],
    data_files=[
        ('', ['README.rst', 'LICENSE']),
    ],
    include_package_data=True,
    provides=["dictools"],
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
