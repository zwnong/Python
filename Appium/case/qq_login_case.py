# coding = utf-8
import threading
import time
import unittest
import HTMLTestRunner
from appium import webdriver

from business.qq_login_business import QQLoginBusiness


class QQLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('this is setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('this is tearDownClass')

    def setUp(self):
        print('this is setUp')

    def tearDown(self):
        print('this is tearDown')

    def test_01(self):
        print('case')
        self.assertEqual(1, 2, msg='1不等于2')


def suite(i):
    suite = unittest.TestSuite()
    suite.addTest(QQLogin("test_01"))
    # 获取当前时间
    # now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:')
    file_path = r'E:\Appium\report\report' + str(i+1) + '.html'
    with open(file_path, 'wb') as ft:
        HTMLTestRunner.HTMLTestRunner(ft).run(suite)


if __name__ == '__main__':
    threads = []
    for i in range(3):
        t = threading.Thread(target=suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
