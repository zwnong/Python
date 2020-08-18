# coding = utf-8
"""
@project: Spider
@author: ZWNONG
@file: yuansu_main.py
@time: 2020-06-19 13:59:46
"""
import re

import requests
from bs4 import BeautifulSoup


class YuanSu:

    def main(self):
        # 启动下载器下载页面将结果存储
        new_url = requests.get('https://www.tukuppt.com/yuansu/', timeout=30)
        # 解析页面 得到新的数据 新的url列表
        soup = BeautifulSoup(new_url.content, 'lxml')
        # 添加url进url管理器
        pic = soup.find_all('img', src=re.compile(r'//img.tukuppt.com/ad_preview/00/06/78/f6EAkcTAJ6.jpg!/fw/260', soup.content))
        # 收集数据
        print(pic)


if __name__ == '__main__':
    test = YuanSu()
    test.main()
