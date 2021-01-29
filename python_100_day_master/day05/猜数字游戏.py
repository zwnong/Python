# coding = utf-8
"""
@All-project: python_100_day_master
@author: ZWNONG
@file: 猜数字游戏.py
@time: 2020-09-04 22:24:42
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

import random

print('计算机出一个1~100之间的随机数由人来猜计算机根据人猜的数字分别给出提示大一点/小一点/猜对了\n')
answer = random.randint(1, 100)
content = 0
while True:
    content += 1
    number = int(input('请输入：'))
    if number < answer:
        print('输入比生成小了一点')
    elif number > answer:
        print('输入比生成大了一点')
    else:
        print('恭喜您答对啦！！')
        break
if content <= 7:
    print('您总共猜了%d次就猜对啦，爱了爱了' % content)
else:
    print('您总共猜了%d次，智商余额明显不足哦' % content)
