#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : spider_day3.py
# @Author: KingJX
# @Date  : 2018/9/1 9:12
""""""
from urllib.parse import quote, unquote

from urllib.robotparser import RobotFileParser

import requests

import re

if __name__ == '__main__':

    '''
    keyword = '壁纸'
    url = 'https://www.baidu.com/s?wd=' + quote(keyword)
    print(url)
    # https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8

    url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
    print(unquote(url))
    '''
    '''
    rp = RobotFileParser()
    rp.set_url('http://www.kingjx.com/robots.txt')
    rp.read()
    print(rp.can_fetch('kingjxSpider', 'http://www.kingjx.com/p/b675544025d7d'))
    print(rp.can_fetch('xiaokSpider', 'http://www.kingjx.com/search?q=python&page=1&type=collections'))
    '''

    '''
    # r = requests.get('http://www.baidu.com')
    r = requests.post('http://httpbin.org/post')
    print(type(r))
    print(r.status_code)
    print(type(r.text))
    print(r.text)
    print(r.cookies)
    '''
    '''
    # r = requests.get('http://httpbin.org/get?name=germey&age=22')
    data = {
        'name': 'germey',
        'age': '22'
    }
    r = requests.get('http://httpbin.org/get', params=data)
    print(r.text)
    try:
        print(r.json())
    except:
        print('返回结果不是json格式的数据')
    '''
    '''
    headers = {
        'User-Agent': 'MOzilla/5.0 (Macintosh; Intel Mac OS x 10_11_4) AppleWebKit/537.36 (KHTML, like. Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    titles = re.findall(pattern, r.text)
    print(titles)
    '''

    r = requests.get('https://github.com/favicon.ico')
    print(r.text)
    print(r.content)
    with open('favicon.ico', 'wb') as f:
        f.write(r.content)