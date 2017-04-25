#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
"""
A command line translator powered by [Youdao api](http://fanyi.youdao.com/openapi).

## usage

1. translator TEXT

The program can be used with a TEXT to be translated followed.

```shell
$translator good
好
---------------------
美音：[ɡʊd]
英音：[gʊd]
更多释义：
n. 好处；善行；慷慨的行为
adj. 好的；优良的；愉快的；虔诚的
adv. 好
n. (Good)人名；(英)古德；(瑞典)戈德
```

2. translator without any args

It can also be used without any args to enter the interactive mode.

```shell
$translator
Enter your text to be translated.Type `q` to quit.
>>hello
你好
---------------------
美音：[hɛˈlo, hə-]
英音：[hə'ləʊ; he-]
更多释义：
n. 表示问候， 惊奇或唤起注意时的用语
int. 喂；哈罗
n. (Hello)人名；(法)埃洛
>>
```
"""
from setuptools import setup

__version__ = '0.0.4'

setup(
	name='mec-translator',
    version=__version__,
    url='https://github.com/mecforlove/translator',
    license='Apache',
    author='mec',
    author_email='mecforlove@outlook.com',
    description='A command line translator powered by Youdao api',
    long_description=__doc__,
    packages=['translator'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    entry_points='''
        [console_scripts]
        translator=translator.translator:main
    '''
)

