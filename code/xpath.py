#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : xpath.py
# @Author: KingJX
# @Date  : 2018/9/8 14:35
""""""

from lxml import etree

if __name__ == '__main__':
    pass


text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">frist item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# 构造一个XPath对象(第五行li标签未闭合, 但是etree模块可以自动修正HTML文本,并且会自动补全html和body标签)
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))

print('===========================')

# 通过xpath来选取符合要求的节点
# //*选取所有标签内容
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)
# //标签 得到所有选取的标签
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li')
print(result)
# @ 选择属性    .. 父标签
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//a[@href="link3.html"]/../@class')
print(result)

