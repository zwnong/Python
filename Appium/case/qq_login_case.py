# coding = utf-8
# 进程
import multiprocessing
import os
import sys

sys.path.append(os.getcwd())
import time
import unittest
import HTMLTestRunner
from base.base_driver import Driver
from util.sever import Server
from util.write_user_command import WriteUserCommand
from business.qq_login_business import QQLoginBusiness


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class QqLoginCase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        cls.qq_login = QQLoginBusiness(parames)

        print('this is setupclass', parames)

    @classmethod
    def tearDownClass(cls):
        base_driver = Driver()
        base_driver.quit_driver(parames)
        print('this is teardowmclass')

    def setUp(self):
        print('this is setup')

    def tearDown(self):
        print('this is teardowm')

    def test_01(self):
        self.qq_login.go_login()
        print('this is case01', parames)

    def test_02(self):
        self.qq_login.login_pass()
        print('this is loginpass')

    def test_03(self):
        self.qq_login.login_fail()
        print("this is loginfail")


def get_count():
    """
    获取yaml文件行数  即字典大小 以启动线程数量
    :return:
    """
    write_user_file = WriteUserCommand()
    count = write_user_file.get_yaml_lines()
    return count


def appium_init():
    server = Server()
    server.main()


def main(i):
    # unittest.main()
    appium_init()
    suite = unittest.TestSuite()
    suite.addTest(QqLoginCase("test_01", parame=i))
    suite.addTest(QqLoginCase("test_02", parame=i))
    file_path = r"E:\github\Python\Appium\report\report" + str(i) + ".html"
    with open(file_path, "wb") as f:
        HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告如下', description='详细').run(suite)


if __name__ == '__main__':
    # # 多线程运行
    # threads = []
    # for i in range(get_count()):
    #     print(i)
    #     t = threading.Thread(target=main, args=(i,))
    #     threads.append(t)
    # for j in threads:
    #     j.start()
    #     time.sleep(1)

    # 多进程运行
    pros = []
    for i in range(get_count()):
        print(i)
        t = multiprocessing.Process(target=main, args=(i,))
        pros.append(t)
    for j in pros:
        j.start()
        time.sleep(1)
