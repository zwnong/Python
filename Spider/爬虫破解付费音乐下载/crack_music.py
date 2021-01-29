# coding = utf-8
"""
@All-project: Spider
@author: ZWNONG
@file: crack_music.py
@time: 2020-07-06 19:43:34
"""
import os
import re
import requests
from bs4 import BeautifulSoup

# 破解付费音乐下载
"""
1、获取目标得url
2、正则提取数据
3、采集数据得规律
4、保存数据 
点击下载会返回登录页面
"""


# 获取url  熊猫办公
class CrackMusic:
    def __init__(self):
        self.music_path = r'E:\music_downlocal/'
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 "
                                      "Safari/537.36 ",
                        "Referer": "http: // www.kuwo.cn / search / list?key = % E9 % BD % 90 % E4 % B8 % 80",
                        "Cookie": "_ga=GA1.2.1671606070.1594624049; _gid=GA1.2.1161225305.1594624049; "
                                  "Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1594624050,1594624747; "
                                  "Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1594624747; kw_token=VE9L6CS7IVR",
                        "csrf": "VE9L6CS7IVR"
                        }
        # self.music_url = music_url  # r'https://www.tukuppt.com/peiyue/'

    def xiongmaobangong(self, music_url):
        # 发送请求
        response = requests.get(url=music_url, headers=self.headers)
        # 提取数据
        html_data = re.findall("""<a  class='title' target="_blank" href=".*?">(.*?)</a>""", response.text)
        play_url = re.findall("""<source src="(.*)" type="audio/mpeg">""", response.text)

        for i in range(0, 40):
            result = requests.get("http:" + play_url[i]).content
            # 写入到文件

            if not os.path.exists(self.music_path):
                os.mkdir(self.music_path)
            name = self.music_path + '/' + html_data[i] + ".mp3"  # ‘/’：标记为文件夹
            with open(name, "wb") as f:
                f.write(result)
                print("正在下载:" + html_data[i])

    def kuwo_music(self):
        singer = input('请输入明星名字:')
        url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=%s&rn=30&httpsStatus=1&reqId=899ddb80-c4da-11ea-a0b9-57482c8af650' % singer
        respones = requests.get(url=url, headers=self.headers).json()
        data = respones["data"]['list']
        for i in data:
            new_url = 'http://www.kuwo.cn/url?format=mp3&rid=i["rid"]&response=url&type=convert_url3&br=128kmp3&from=web&t=1594625347901&httpsStatus=1&reqId=899e9ed1-c4da-11ea-a0b9-57482c8af650'
            result = requests.get(new_url, self.headers).json()
            print(result)

    def kugou_music(self):
        headers = {
            ":authority": "complexsearch.kugou.com",
            ": scheme": "https",
            "accept": "* / *",
            "accept - encoding": "gzip, deflate, br",
            "accept - language": "zh - CN, zh;",
            "cookie": "kg_mid=70e2bd2d75baa16a40a05c37cf89be32; kg_dfid=1IMM8Y1DVnKZ0zKyhh1Z3vUP; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; "
                      "Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1594565437,1594613838,1594614928,1594878015; "
                      "kg_mid_temp=70e2bd2d75baa16a40a05c37cf89be32; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1594878064",
            "referer": 'https://www.kugou.com/yy/html/search.html'

        }
        url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&keyword=%E8%BF%99%E4%B8%AA%E5%B9%B4%E7%BA%AA&page=1&pagesize=30&bitrate=0&isfuzzy=0&tag=em&inputtype=0&platform=WebFilter&userid=-1&clientver=2000&iscorrection=1&privilege_filter=0&srcappid=2919&clienttime=1594878137006&mid=1594878137006&uuid=1594878137006&dfid=-&signature=7F2253FAAABED8E8EEB3B5C32F4283BD'
        data = requests.get(url, headers)
        print(data)


if __name__ == '__main__':
    run = CrackMusic()
    run.kugou_music()
