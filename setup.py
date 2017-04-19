#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
from setuptools import setup


__version__ = '0.0.1'

setup(
	name='Translator',
    version=__version__,
    url='https://github.com/mecforlove/translator',
    license='Apache',
    author='mec',
    author_email='mecforlove@outlook.com',
    description='A command line translator powered by Youdao api',
    long_description=open('README.md').read(),
    packages=['translator'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    entry_points='''
        [console_scripts]
        translator=translator.translator:main
    '''
)

