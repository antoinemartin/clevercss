#!/usr/bin/env python
from setuptools import setup
import os

fp = open(os.path.join(os.path.dirname(__file__), "README.rst"))
readme_text = fp.read()
fp.close()

setup(
    name='CleverCSS',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    maintainer='David Ziegler',
    maintainer_email='david.ziegler@gmail.com',
    version='0.3',
    url='http://sandbox.pocoo.org/clevercss/',
    download_url='http://github.com/antoinemartin/clevercss/tree',
    py_modules = [ 'extract_sprites' ],
    packages=['clevercss'],
    install_requires=['cssutils'],
    entry_points = {
        'console_scripts': [ 'ccss = clevercss.ccss:main' ]
    },
    description='python inspired sass-like css preprocessor',
    long_description=readme_text,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python'
    ],
    test_suite = 'tests.all_tests',
)
