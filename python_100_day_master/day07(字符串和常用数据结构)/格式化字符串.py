# coding = utf-8
"""
@All-project: python_100_day_master
@author: ZWNONG
@file: 格式化字符串.py
@time: 2020-09-06 14:57:55
"""
# 1 %d
a, b = 5, 10
print('%d * %d = %d'% (a, b, a * b))

# 2 .format()
print('{0} * {1} = {2}'.format(a, b, a * b))

# 3 f
print(f'{a} * {b} = {a * b}')
