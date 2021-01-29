# coding = utf-8
"""
@All-project: python_100_day_master
@author: ZWNONG
@file: 常用模块.py
@time: 2020-09-04 23:06:20
"""
'''
python 常用模块
- 运行是服务模块相关：copy / pickle / sys / ...
- 数学模块相关： decimal / math / random / ...
- 字符串处理模块： codecs / re / ...
- 文件处理相关模块：shutil / gzip /...
- 操作系统相关服务：datetime / threading / queue
- 进行和线程相关：multiprocessing / threading / queue
- 网络应用相关模块：ftplib / http / smtplib / urllib/  ...
- web编程相关：cgi / webbrower
- 数据处理和编码相关：base64 / csv / html.parser / json / xml /..
'''

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)

asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
print(asctime)
