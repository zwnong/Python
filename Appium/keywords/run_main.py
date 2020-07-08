# coding = utf-8
"""
@project: Appium
@author: ZWNONG
@file: run_main.py
@time: 2020-07-01 12:59:28
"""
from keywords.get_data import GetData
from keywords.action_method import ActionMethod
from util.sever import Server


# 关键字模型程序入口
class RunMain:
    def __init__(self):
        self.action_method = ActionMethod()
        self.data = GetData()
        self.server = Server()

    def run_method(self):
        self.server.main()
        lines = self.data.get_case_lines()
        for i in range(1, lines):
            handle_step = self.data.get_handle_step(i)


if __name__ == '__main__':
    run = RunMain()
    run.run_method()
