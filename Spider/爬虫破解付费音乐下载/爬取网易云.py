# coding = utf-8
"""
@project: Spider
@author: ZWNONG
@file: 爬取网易云.py
@time: 2020-10-13 19:56:56
"""
import requests
from lxml import etree  # 解析/处理响应数据
import time

"""#  步骤：
#  1、发送请求
#  2、接受并解析网站响应结果
#  3、筛选需要的数据
#  4、将帅选出来的数据保存到本地"""

singer_id = input("请输入需要爬取的歌手的id：")
#  https://music.163.com/#/artist?id=6452
url = 'https://music.163.com/artist?id=' + singer_id  # 每一个歌手的音乐都是id在变

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
}

#  1、发送请求
response = requests.get(url, headers=headers)

#  2、接受并解析网站响应结果
html_text = response.content.decode('utf-8')

#  3、筛选需要的数据
html = etree.HTML(html_text)
music_lists = html.xpath('//a[contains(@href,"/song?")]')
downmusic_url = 'http://music.163.com/song/media/outer/url?id='
path = r'E:\网易云音乐\黄家驹'
try:
    for m in music_lists:
        href = m.xpath('./@href')[0]
        music_id = href.split('=')[1]
        #  音乐的名字
        music_name = m.xpath('./text()')[0]
        music_url = downmusic_url + music_id
        music_resp = requests.get(music_url, headers=headers)
        with open(path + '\\' + music_name + '.mp3', 'wb') as f:
            f.write(music_resp.content)
            print('《' + music_name + '》 下载完成...')
            time.sleep(1)
except EOFError:
    print('finish')
