#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requirements

from setuptools import find_packages, setup

exec(open('steenzout/serialization/json/metadata.py').read())


def install_requires(file_name):
    """
    Parse the requirements.txt file

    Returns:
        list: parsed requirements.txt
    """
    required_packages = []
    with open(file_name, 'r') as f:
        for i in requirements.parse(f):
            if i.name:
                if i.editable: # has an -e at the beginning
                    required_packages.append(i.name)
                else:
                    required_packages.append(i.line)
    return required_packages


setup(
    name='steenzout.serialization.json',
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    maintainer=__maintainer__,
    maintainer_email=__maintainer_email__,
    url=__url__,
    namespace_packages=['steenzout'],
    packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
    package_data={'': ['LICENSE', 'NOTICE.md']},
    install_requires=install_requires('requirements.txt'),
    tests_require=install_requires('requirements-test.txt'),
    license=__license__,
    classifiers=__classifiers__)
