# coding = utf-8

import html_output
import html_parser
import url_manager

"""
@project: Spider
@author: ZWNONG
@file: spider_main.py
@time: 2020-06-19 12:07:02
"""


# 爬虫调度器
class SpiderMain:
    def __init__(self, html_downloader, html_outputer):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDowmder()
        self.parser = html_parser.HtmlPaeser()
        self.outputer = html_output.HtmlOutputer()

    def craw(self, root_url):
        """
        总调度程序
        :param root_url:
        :return:
        """
        # 将root_url添加进url
        self.urls.add_new_url(root_url)
        # 记录当前是第几个url
        count = 1
        # 当管理器中有未爬取的url
        while self.urls.has_new_url():
            try:
                # 获取一个url
                new_url = self.urls.get_new_url()
                print('crwa %d : %s' % (count, new_url))
                # 启动下载器下载页面将结果存储
                html_cont = self.downloader.download(new_url)
                # 解析页面 得到新的数据 新的url列表
                new_data = self.parser.parse(new_url)
                new_urls = self.parser.parse(html_cont)
                # 添加url进url管理器
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count += 1
            except:
                print("fail")

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://www.tukuppt.com/yuansu/'  # 入口URL
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
