# coding = utf-8
"""
@project: Spider
@author: zwnong
@file: picture.py
@time: 2020-06-13 11:07:51
"""
import requests
import os
import re
from pypinyin import lazy_pinyin


class GetPictuer:

    def getHTMLText(self, url):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            print(" ")

    def getPageUrls(self, text, name):
        re_pageUrl = r'href="(.+)">\s*<img src="(.+)" alt="' + name
        return re.findall(re_pageUrl, text)

    def dowmPictures(self, text, root, name):
        pageUrls = self.getPageUrls(text, name)
        titles = re.findall(r'alt="' + name + r'(.+)" ', text)
        for i in range(len(pageUrls)):
            pageUrl = pageUrls[i][0]
            path = root + titles[i] + "//"
            if not os.path.exists(path):
                os.mkdir(path)
            if not os.listdir(path):
                pageText = self.getHTMLText(pageUrl)
                totalPics = int(re.findall(r'<em>(.+)</em>）', pageText)[0])
                downUrl = re.findall(r'href="(.+?)" class="">下载图片', pageText)[0]
                cnt = 1
                while cnt <= totalPics:
                    picPath = path + str(cnt) + ".jpg"
                    r = requests.get(downUrl)
                    with open(picPath, 'wb') as f:
                        f.write(r.content)
                        f.close()
                    print('{} - 第{}张下载已完成\n'.format(titles[i], cnt))
                    cnt += 1
                    nextPageUrl = re.findall(r'href="(.+?)">下一张', pageText)[0]
                    pageText = self.getHTMLText(nextPageUrl)
                    downUrl = re.findall(r'href="(.+?)" class="">下载图片', pageText)[0]
        return

    def run(self):
        name = input("输入需要下载的明星的名字:")
        nameUrl = "http://www.win4000.com/mt/" + ''.join(lazy_pinyin(name)) + ".html"
        try:
            text = self.getHTMLText(nameUrl)
            if not re.findall(r'暂无(.+)!', text):
                root = "F://pics//" + name + "//"
                if not os.path.exists(root):
                    os.mkdir(root)
                self.dowmPictures(text, root, name)
                try:
                    nextPage = re.findall(r'next" href="(.+)"', text)[0]
                    while nextPage:
                        nextText = self.getHTMLText(nextPage)
                        self.dowmPictures(nextText, root, name)
                        nextPage = re.findall(r'next" href="(.+)"', nextText)[0]
                except IndexError:
                    print("已全部下载完毕")
        except TypeError:
            print("不好意思，没有{}的照片".format(name))
        return


if __name__ == '__main__':
    run = GetPictuer()
    run.run()
