# coding = utf-8

import unittest
import HTMLTestRunner
from business.qq_go_login_business import QqGoLoginBusiness


class QqLoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = QqGoLoginBusiness()

        print('this is setupclass')

    @classmethod
    def tearDownClass(cls):

        print('this is teardowmclass')

    def setUp(self):
        print('this is setup')

    def tearDown(self):
        print('this is teardowm')

    def test_01(self):
        self.login.go_login()
        self.login.qq_login_pass()
        print('this is case01')

    def test_02(self):
        print('this is case02')

    def main(self):
        # unittest.main()
        suite = unittest.TestSuite()
        suite.addTest(QqLoginCase("test_01"))
        suite.addTest(QqLoginCase("test_02"))
        file_path = r"E:\github\Python\Appium\report\result.html"
        with open(file_path, "wb") as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告如下', description='详细').run(suite)


if __name__ == '__main__':
    run = QqLoginCase()
    run.main()
