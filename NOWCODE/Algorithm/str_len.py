# coding = utf-8
def str_len():
    """
    计算字符串最后一个单词的长度，单词以空格隔开
    :return:
    """
    str1 = str(input('input:'))
    if 0 < len(str1) < 10:
        value = len(str1.strip().split(' ')[-1])
        return value
    else:
        print('re_input:')


print(str_len())
