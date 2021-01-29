# coding = utf-8
"""
@All-project: python_100_day_master
@author: ZWNONG
@file: 判断是不是闰年.py
@time: 2020-09-03 15:50:54
"""
# 输入年份，判断该年份是不是闰年
year = int(input('请输入年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('输入的年份是 闰年')
else:
    print('输入的年份不是 闰年')
