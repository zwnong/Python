# coding = utf-8
"""
@project: Reptile
@author: ZWNONG
@file: crack_music.py
@time: 2020-07-06 19:43:34
"""
import os
import re
import requests

# 破解付费音乐下载
"""
1、获取目标得url
2、正则提取数据
3、采集数据得规律
4、保存数据 
点击下载会返回登录页面
"""
# 获取url  熊猫办公
music_url = r'https://www.tukuppt.com/peiyue/'
# 发送请求
response = requests.get(url=music_url)
# 提取数据
html_data = re.findall("""<a  class='title' target="_blank" href=".*?">(.*?)</a>""", response.text)
play_url = re.findall("""<source src="(.*)" type="audio/mpeg">""", response.text)

for i in range(0, 40):
    result = requests.get("http:"+play_url[i]).content
    # 写入到文件
    music_path = r'E:\music_downlocal'
    if not os.path.exists(music_path):
        os.mkdir(music_path)
    name = music_path + '/' + html_data[i] + ".mp3"  # ‘/’：标记为文件夹
    with open(name, "wb") as f:
        f.write(result)
        print("正在下载:" + html_data[i])

