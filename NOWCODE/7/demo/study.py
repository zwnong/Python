# coding = utf-8

# 第七章 字符串与正则表达式

"""
使用'+'拼接字符串
# 字符串不允许直接与其他类型的数据链接
"""
cn = 'Life is short, I use python'
en = '人生苦短，我用python'
numb = 123
print(cn + '---' + str(numb) + en)

'''
计算字符串的长度
'''
print('cn与en拼接后的长度为：', len(cn + en))
print('cn与en拼接后编码utf-8的长度为：', len(cn.encode() + en.encode()))
print('cn与en拼接后编码GBK的长度为：', len(cn.encode('gbk') + en.encode('gbk')))

'''
截取字符串
语法格式：string[start: end : step]
string表示：要截取的字符串
start表示：要截取的第一个字符串的索引（包括该字符串），如果不指定，则默认为0
end表示：包截取的最后宇哥字符串的索引（不包括该字符串），如果不指定则默认最长度
step表示：切片的长度，如果省略，默认为1
'''
str_qiepian = cn + ':' + en
try:
    print('截取第二个字符串：', str_qiepian[1])
    print('从第27个字符串开始截取：', str_qiepian[27:])
    print('从左边开始截取27个字符串：', str_qiepian[:27])
    print('截取第28个到第31个字符串：', str_qiepian[27:31])
except IndexError:
    print('指定的索引不存在')

'''
分割字符串：split() ， 返回值为列表
语法：str.split(sep, maxsplit)
sep:指定分割字符，
maxsplit:分割的次数
'''
print('默认分割:', str_qiepian.split())
print('英文与中文分割:', str_qiepian.split(':'))
print('采用空格分割，并且只分割3次:', str_qiepian.split(' ', 3))

'''
检索字符串
'''
# count(): 用于检索指定字符串在另一个字符串的出现的次数,如果不存在 则返回0
print('p出现的次数:', str_qiepian.count('p'))

# find(): 检索是否包含指定字符串的索引（第一次出现），如果不存在，则返回-1，
print('find检索，第一次出现包含指定字符串的索引:', str_qiepian.find('y'))

# indxe() 与find()方法类似，只不过当指定的字符串不存在会抛出异常
print('index检索字符串', str_qiepian.index('y'))

# startswith() 检索字符串是否以指定的字符串开头，结果为布尔值
print('startswith检索指定字符串是否是开头:', str_qiepian.startswith('y'))

