# coding = utf-8
"""
@All-project: python_100_day_master
@author: ZWNONG
@file: 最大公约数最小公倍数.py
@time: 2020-09-04 22:55:50
"""


# 函数的定义和使用 - 求最大公约数和最小公倍数
def gcd(x, y):
    if x > y:
        # 如果x>y xy值互换
        (x, y) = (y, x)
    for f in range(x, 1, -1):
        if x % f == 0 and y % f == 0:
            return f
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))
