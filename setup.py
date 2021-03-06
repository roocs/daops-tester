#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

__author__ = "YOUR NAME"
__contact__ = "YOUR EMAIL"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__version__ = "0.1.0"


# One strategy for storing the overall version is to put it in the top-level
# package's __init__ but Nb. __init__.py files are not needed to declare
# packages in Python 3


# Populate long description setting with content of README
#
# Use markdown format read me file as GitHub will render it automatically
# on package page
with open("README.md") as readme_file:
    _long_description = readme_file.read()


requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]


setup(
    author=__author__,
    author_email=__contact__,

    # See:
    # https://www.python.org/dev/peps/pep-0301/#distutils-trove-classification
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description="A short description goes here",

    license=__license__,

    # This qualifier can be used to selectively exclude Python versions -
    # in this case early Python 2 and 3 releases
    python_requires='>=3.5.0',
    entry_points={
        'console_scripts': [
            'daops_tester=daops_tester.cli:main',
        ],
    },
    install_requires=[
        requirements,
        "roocs_utils @ git+https://github.com/roocs/roocs-utils.git",
    ],
    long_description=_long_description,
    long_description_content_type='text/markdown',

    include_package_data=True,
    keywords='daops_tester',
    name='daops_tester',
    packages=find_packages(),
    package_data={"daops_tester": ["etc/roocs.ini"]},
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/roocs/daops-tester',
    version=__version__,
    zip_safe=False,
)
