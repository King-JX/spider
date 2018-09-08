#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : spider_day2.py
# @Author: KingJX
# @Date  : 2018/8/30 19:36
""""""

'''
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)
try:
    response = opener.open('https://www.baidu.com')
    print(response.read().decode('utd-8'))
except URLError as e:
    print(e.reason)
'''

# import  http.cookiejar, urllib.request

'''====================获取网站的cookie==================='''
'''
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+'='+item.value)
'''

'''====================以文本的格式保存cookie================='''
'''
# 1.MozillaCookieJar
filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)

# 2.LWPCookieJar
filename = 'cookie2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response1 = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
'''

'''===============获取生成的Cookie文本中的有用的信息======================'''
'''
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie2.txt', ignore_expires=True, ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
'''

# from urllib import request,error
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')



from urllib.parse import urlparse
result = urlparse('http://www.baidu.com/index.html;user?id=#comment')
print(type(result), result, sep='\n')






