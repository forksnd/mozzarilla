#!/usr/bin/env python
from os.path import dirname, join
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

curr_dir = dirname(__file__)

import mozzarilla


try:
    try:
        long_desc = open(join(curr_dir, "readme.rst")).read()
    except Exception:
        long_desc = "Since PyPI refuses to let me upload due to my readme being Markdown, I wont be using a readme."
        #long_desc = open(join(curr_dir, "readme.md")).read()
except Exception:
    long_desc = 'Could not read long description from readme.'

setup(
    name='mozzarilla',
    description='A variant of Binilla for editing binary structures for \
games built with the Blam engine.',
    long_description=long_desc,
    version='%s.%s.%s' % mozzarilla.__version__,
    url='http://bitbucket.org/moses_of_egypt/mozzarilla',
    author='Devin Bobadilla',
    author_email='MosesBobadilla@gmail.com',
    license='MIT',
    packages=[
        'mozzarilla',
        'mozzarilla.defs',
        'mozzarilla.widgets',
        'mozzarilla.widgets.field_widgets',
        'mozzarilla.windows',
        'mozzarilla.windows.tools',
        'mozzarilla.windows.tag_converters',
        ],
    package_data={
        '': ['*.txt', '*.md', '*.rst', '*.pyw', '*.ico', '*.png', 'msg.dat'],
        'mozzarilla': [
            'styles/*.*',
            ]
        },
    platforms=["POSIX", "Windows"],
    keywords="binilla, binary, data structure",
    install_requires=['reclaimer>=2.6.0', 'binilla>=1.2.0'],
    requires=['reclaimer>=2.6.0', 'binilla>=1.2.0'],
    provides=['mozzarilla'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        ],
    zip_safe=False,
    )
