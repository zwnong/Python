# coding = utf-8

import requests
from bs4 import BeautifulSoup


class Request:

    # 请求方式

    def get(self):
        """
        get请求
        :return:
        """

    # 发送不带参数的get请求
    # re = requests.get('https://github.com/zwnong/Python')
    # print(re.text)

    # 发送带参数的get请求
    re1 = requests.get(url='https://github.com/zwnong/Python', params={'wb': 'python'})
    data = re1.text
    soup = BeautifulSoup(data, "html.parser")
    # print(soup)
    # print(soup.prettify())

    # 获得一个beautiful对象之后
    """
    # 提取html信息
    """
    # print(soup.tltle)  # 获取html的title信息
    # print(soup.a)  # 获取a标签，默认获取第一个a标签信息 若想获取全部 用for遍历
    # print(soup.a.name)  # 获取a标签的名字
    # print(soup.a.parent.name)  # 获取a标签的父标签（上一级）的名字

    # print('a标签的类型：', type(soup.a))
    # print('第一个a标签的属性:', soup.a.attrs)
    # print('a标签属性的类型:', type(soup.a.attrs))
    # print('a标签的class属性:', soup.a.attrs['class'])    # 因为是字典，通过字典的方式获取a标签的class属性
    # print('a标签的href属性:', soup.a.attrs['href'])      # 同样是字典，通过字典的方式获取a标签的href属性

    # print('第一个a标签的内容:', soup.a.string)  # a标签的非属性字符串信息，表示尖括号之间的那部分字符串
    # # 所有a标签的内容
    # # for i in soup.text:
    # #     print(soup.a.name)
    #
    # print('a标签的非属性字符串的类型:', type(soup.a.string))  # 查看标签string字符串的类型
    #
    # print('a标签第一个人p标签标签的内容:', soup.p.string)  # p标签字符串信息（注意p标签中还有b标签，但是打印string时并没有b标签，说明string类型可以跨多个标签层次）

    """
    find_all():
        name 对标签名称的检索字符串
        attrs 对标签属性的值得检索字符串，可以标注属性检索
        recursive 是否对子孙全部检索，默认为True
        string <>..</> 中字符串区域的检索字符串
    """
    print('所有a标签的内容:', soup.find_all('a'))  # 返回一个列表类型
    print('a和b标签的内容:', soup.find_all('a', 'b'))

    def post(self):
        """
        post请求
        :return:
        """
        requests.post('https://github.com/zwnong/Python')

    def put(self):
        """
        put请求
        :return:
        """
        requests.put("https://github.com/zwnong/Python")

    def delete(self):
        """
        delete请求
        :return:
        """
        requests.delete("https://github.com/zwnong/Python")

    def head(self):
        """
        head请求
        :return:
        """
        requests.head("https://github.com/zwnong/Python")

    def options(self):
        """
        options请求
        :return:
        """
        requests.options("https://github.com/zwnong/Python")


if __name__ == '__main__':
    request = Request()
    request.get()
