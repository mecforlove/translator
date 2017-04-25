#!/usr/bin/python  
# -*- coding:utf-8 -*-  
# File Name: translator.py
# Author: meczhang
# Mail: mecforlove@outlook.com
# Created Time: 2016-08-11 19:03:20
import sys
import urllib2
import json
import urllib
import readline

# config
YOUDAO_URL = 'http://fanyi.youdao.com/openapi.do?'
KEYFORM = 'letusgo'
KEY = '68421793'


def translate(text):
    """翻译接口调用

    :param text: 待翻译的文本
    :type text: str
    :return: api原始响应的dict
    """
    req_params = dict(
        keyfrom=KEYFORM,
        key=KEY,
        type='data',
        doctype='json',
        version='1.1',
        q=text
    )
    url = YOUDAO_URL + urllib.urlencode(req_params)
    resp = urllib2.urlopen(url=url)
    data = json.loads(resp.read())
    return data


class View(object):
    """表现层
    ~~~~~~~~~~~~~~~~~
    用于翻译结果的展示
    """
    def __init__(self, data):
        self.data = data

    @property
    def translation(self):
        return ', '.join(self.data['translation'])

    @property
    def basic(self):
        if 'basic' not in self.data:
            return ''
        basic_dict = self.data['basic']
        explains = '\n'.join(basic_dict.get('explains', ''))
        return u"""\
美音：[{us_phonetic}]
英音：[{uk_phonetic}]
更多释义：
{explains}""".format(us_phonetic=basic_dict.get('us-phonetic', ''),
                     uk_phonetic=basic_dict.get('uk-phonetic', ''),
                     explains=explains)


def main():
    args = sys.argv
    if len(args) > 1:
        text = ''.join(args[1:])
        view = View(translate(text))
        print view.translation
        print '---------------------'
        print view.basic
        sys.exit(0)
    print 'Enter your text to be translated.Type `q` to quit.'
    while True:
        text = raw_input('\033[36m>>\033[0m').strip()
        if text == 'q':
            print 'Bye!'
            sys.exit(0)
        if not len(text):
            continue
        view = View(translate(text))
        print view.translation.encode('utf-8')
        print '---------------------'
        print view.basic.encode('utf-8')




if __name__ == '__main__':
    main()
