# coding = utf-8
"""
@project: python_100_day_master
@author: ZWNONG
@file: 用户身份验证.py
@time: 2020-09-04 10:12:25
"""
username = input('请输入用户名：')
password = input('请输入密码：')
if username == 'admin' and password == '123456':
    print('身份验证成功')
else:
    print('身份验证失败,请重新输入')
