# coding = utf-8
"""
@project: python_100_day_master
@author: ZWNONG
@file: for求和.py
@time: 2020-09-04 10:38:12
"""


# 输入一个整型, 求和
class Sum:
    def __init__(self):
        self.number = int(input('请输入一个整数：'))

    def even(self):
        # 求偶数和
        for i in range(2, self.number, 2):
            self.number += i
        print('偶数之和为：', self.number)

    def odd_number(self):
        # 求奇数和
        for i in range(1, self.number, 2):
            self.number += i
        print('奇数之和为:', self.number)


if __name__ == '__main__':
    test = Sum()
    test.even()
    test.odd_number()
