# -*- coding: utf-8 -*-
# @File  : spider_day4.py
# @Author: KingJX
# @Date  : 2018/9/8 10:03
""""""

import requests
import re
import json
import time
from requests.exceptions import RequestException

# 获取一个网页的内容
def get_one_page(url):

    # 建立一个headers请求头, 来伪装操作系统和浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Inter Mac OS X 10_13_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    # 通过get方式请求网页上的数据
    response = requests.get(url, headers=headers)
    # 判断网页请求是否成功, 成功则返回网页中的文本信息
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    # 通过正则表达式提取想要的内容(排名, 图片, 名称, 主演, 发布时间, 评分)
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>\
(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?\
fraction.*?>(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        # 使用迭代器将得到的结果遍历为字典
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

def write_to_file(content):
    # 写入爬取内容到文本中
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)



if __name__ == '__main__':
    for i in range(10):
        main(offset=i *10)
        time.sleep(1)
