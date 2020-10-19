# coding = utf-8
"""
@project: python_100_day_master
@author: ZWNONG
@file: 列表.py
@time: 2020-09-06 15:39:42
"""
import random

list1 = []
for i in range(20):
    answer = random.randint(1, 100)
    list1.append(answer)

print('随机生成1到100内的20个整数：', list1)


