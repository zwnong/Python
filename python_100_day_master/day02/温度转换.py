# coding = utf-8
"""
@project: python_100_day_master
@author: ZWNONG
@file: 温度转换.py
@time: 2020-09-03 15:39:45
"""
# 华氏温度转换为摄氏温度：$C=(F-32)\div 1.8$

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%s.1f华氏度 = %.1f摄氏度' % (f, c))
