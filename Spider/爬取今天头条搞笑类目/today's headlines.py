# coding = utf-8
"""
@project: Spider
@author: ZWNONG
@file: today's headlines.py
@time: 2020-07-09 14:16:36
"""
import os
import re
import requests
from bs4 import BeautifulSoup

url = r'http://xiaohua.zol.com.cn/new/1.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
response = requests.get(url)

data = re.findall("""'window.collectEvent('start')'""", response.text)
print(data)
