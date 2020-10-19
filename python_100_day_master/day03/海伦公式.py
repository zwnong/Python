# coding = utf-8
"""
@project: python_100_day_master
@author: ZWNONG
@file: 海伦公式.py
@time: 2020-09-04 10:25:25
"""
# 输入三条边，如果构成三角形 则计算周长和面积

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长：%f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积：% f' % area)
else:
    print('不能构成三角形')
