#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : spider_day1.py
# @Author: KingJX
# @Date  : 2018/8/29 22:43
""""""




# urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*, cafile=None, capath=None, cadefault=False, context=None)
# urlopen()利用它可以模拟浏览器的一个请求发起过程.

from urllib import parse
from urllib import request
import urllib
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

'''=====================1.爬取python官网主界面中的内容====================='''
'''
response = urllib.request.urlopen('http://www.kingjx.com')
print(response.read().decode('utf-8'))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
'''

'''=========================2.urlopen()方法中的data参数========================='''
#   将文件转换为二进制, 以表单的方式进行提交
'''
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('https://httpbin.org/post', data=data)
print(response.read())
'''

'''=========================3.urlopen()方法中的timeout参数========================='''
#   设置超时时间, 控制一个网页如果长时间未响应, 就跳过它的抓取, 让爬去更加效率
'''
response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())
'''
'''
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))
'''

'''
url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
'''

'''====================4.爬取有验证的网页========================='''

'''
username = 'username'
password = 'password'
url = 'https://user.qzone.qq.com/1432008567?_t_=0.5845765319742413'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
a_h = HTTPBasicAuthHandler(p)
opener = build_opener(a_h)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)

'''