# coding = utf-8
"""
@project: python_100_day_master
@author: ZWNONG
@file: 素数.py
@time: 2020-09-04 22:42:32
"""
# 输出 2到n之间的素数

import math

print('输出 2到n之间的素数(素数指的是只能被1和自身整除的正整数（不包括1））')
n = int(input('请输入n:'))
for num in range(2, n):
    is_prime = True
    for f in range(2, int(math.sqrt(num)) + 1):
        if num % f == 0:
            is_prime = False
    if is_prime:
        print(num, end=' ')
