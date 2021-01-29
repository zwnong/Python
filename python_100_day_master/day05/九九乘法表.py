# coding = utf-8
"""
@All-project: python_100_day_master
@author: ZWNONG
@file: 九九乘法表.py
@time: 2020-09-04 22:49:47
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d%d%d' % (i, j, i * j), end='\t')
    print()
