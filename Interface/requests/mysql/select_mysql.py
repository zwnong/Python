# coding = utf-8
"""
@project: Interface
@author: ZWNONG
@file: select_mysql.py
@time: 2020-08-29 14:26:10
"""
import pymysql.connections


class SelectMySql:
    def __init__(self):
        self.mydb = pymysql.connect(host="127.0.0.1", user="administrator", passwd="zwnong1234")

    def show_from(self):
        """
        查看数据库
        :return: 
        """
        return self.mydb

    def select(self, form):
        pass


if __name__ == '__main__':
    run = SelectMySql()
    print(run.show_from())
