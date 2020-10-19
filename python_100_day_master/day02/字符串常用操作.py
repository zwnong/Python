# coding = utf-8
"""
@project: python_100_day_master
@author: ZWNONG
@file: 字符串常用操作.py
@time: 2020-09-03 15:56:38
"""
# 字符串常用操作

str1 = 'hello world!'
print('字符串的长度：', len(str1))
print('单词首字母大写：', str1.title())
print('字符串变大写：', str1.upper())
print('字符串是不是大写：', str1.isupper())
print('字符串是不是以hello开头：', str1.endswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))


