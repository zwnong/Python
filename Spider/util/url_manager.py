# coding = utf-8
"""
@All-project: Spider
@author: ZWNONG
@file: url_manager.py
@time: 2020-06-19 14:07:04
"""


class UrlManager:
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, root_url):
        if root_url is None:
            return
        if root_url not in self.new_urls and root_url not in self.old_urls:
            self.new_urls.add(root_url)

    def add_new_urls(self, new_urls):
        if new_urls is None or len(new_urls) == 0:
            return
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        # pop() 会从列表中获取url并且移除重复url
        new_url = self.new_urls.pop()
        # 将新的url添加进oldurl
        self.old_urls.add(new_url)
        return new_url

