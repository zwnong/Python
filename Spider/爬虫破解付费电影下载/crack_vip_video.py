# coding = utf-8
"""
@All-project: Spider
@author: ZWNONG
@file: crack_vip_video.py
@time: 2020-07-04 14:17:57
"""
# 破解视频平台的vip 免费下载
import subprocess

import requests
import re
import os
from pytube import YouTube
from pprint import pprint

"""
# 爬虫下载：找到视频下载链接
# 全名解析：jx.615g.com
# .ts 6s视频文件
# 用ffmpeg.exe合成视频(合成.ts文件)
#
# 比如你用下面的第一个接口地址：http://jx.618g.com/?url=
# 然后VIP电影链接如：https://www.iqiyi.com/v_19rsho8w7c.html
# 合成的链接就是：http://jx.618g.com/?url=https://www.iqiyi.com/v_19rsho8w7c.html"""


# viceo = r'http://jx.618g.com/?url=https://www.iqiyi.com/v_19rrmq9meo.html'
# response = requests.get(viceo).text
# # 提取.m3u8文件 re : 规则  从哪里去找
# # .* 匹配任意字符 url = .m3u8地址链接
#
# m3u8_url = re.search(r"url=(.*m3u8)", response).group(1)  # 搜索有.m3u8结尾的字符 search 只提取一个， ()表示提取（）里的内容
# print(m3u8_url)
#
# # 利用ffmpeg下载视频  ffmpeg -i +.m3u8链接 -vcdodec copy -acdodec copy 取名视频名称.mp4       -vcdodec copy：合成视频；acdodec copy合成音频
# command = '"ffmpeg -i" +url+  -vcdodec copy -acdodec copy 取名视频名称.mp4'
# # subprocess 模拟终端文件下载
# subprocess.call(command, shell=True)
# video_url = r'http://jx.618g.com/?url=https://www.iqiyi.com/v_19rrmq9meo.html'
# response = requests.get(video_url).text
# m3u8_url = re.search(r"url=(.*m3u8)", response).group(1)
# print(m3u8_url)


class CrackVideo:
    def get_m3u8(self, url):
        video_url = r'http://jx.618g.com/?url=' + url
        response = requests.get(video_url).text
        m3u8_url = re.search(r"url=(.*m3u8)", response).group(1)
        return m3u8_url

    #
    #     def run_ffmpeg(self):
    #         os.system(r'爬虫破解付费电影下载/ffmpeg.exe')
    #
    #     def get_video(self, url=None):
    #         self.run_ffmpeg()
    #         if url is None:
    #             url = input('请输入网址:')
    #         m3u8_url = self.get_m3u8(url)
    #         video_path = r'G:\reptile_video'
    #         if not os.path.exists(video_path):
    #             os.chdir(video_path)
    #         command = 'ffmpeg -i' + m3u8_url + '-vcdodec copy -acdodec copy' + video_path
    #         subprocess.call(command, shell=True)
    #
    #
    def get_youtube_video(self):
        m3u8 = self.get_m3u8('http://www.51gcw.com/v/29464.html')
        print(m3u8)


if __name__ == '__main__':
    run = CrackVideo()
    run.get_youtube_video()
