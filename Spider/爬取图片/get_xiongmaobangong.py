# coding = utf-8
"""
@All-project: Spider
@author: ZWNONG
@file: get_xiongmaobangong.py
@time: 2020-07-07 10:22:15
"""
import requests
import re

url = r'https://www.tukuppt.com/yuansu/g101/zonghe_0_0_0_0_0_0_2.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
print(response.text)
data = re.findall('''<a class='img img-ys' style="height:260px;" href="/muban/jpmzyamk.html" target="_blank">
<img title="简约创意音符" class="lazy"  data-original="//img.tukuppt.com/ad_preview/00/11/76/9ohkaxKojp.jpg!/fw/260" ><div class='mark'></div></a>''', response.text)

print(data)
