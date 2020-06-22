# coding = utf-8
"""
@project: Reptile
@author: ZWNONG
@file: html_downloader.py
@time: 2020-06-19 12:10:06
"""
import requests
from bs4 import BeautifulSoup


# URL下载器

class HtmlDownloader:
    def download(self, url):
        if url is None:
            return None

        response = requests.get(url)
        if response.status_code != 200:
            return None
        return print(response.content)


if __name__ == '__main__':
    test = HtmlDownloader()
    test.download('http://www.baidu.com')
