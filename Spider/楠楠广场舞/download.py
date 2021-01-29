# coding = utf-8
"""
@All-project: github
@author: ZWNONG
@file: download.py
@time: 2020-08-13 11:11:27
"""
# 广场舞下载
import re
import subprocess
import requests

"""
# 爬虫下载：找到视频下载链接
# 全名解析：jx.615g.com
# .ts 6s视频文件
# 用ffmpeg.exe合成视频(合成.ts文件)
#
# 比如你用下面的第一个接口地址：http://jx.618g.com/?url=
# 然后VIP电影链接如：https://www.iqiyi.com/v_19rsho8w7c.html
# 合成的链接就是：http://jx.618g.com/?url=https://www.iqiyi.com/v_19rsho8w7c.html"""

video = r'http://jx.618g.com/?url=https://www.iqiyi.com/v_19rsho8w7c.html'
response = requests.get(video).text
m3u8_url = re.findall(r"url=(.*m3u8)", response)
print(m3u8_url)

