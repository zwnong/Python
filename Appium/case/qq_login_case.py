# coding = utf-8

import unittest
import HTMLTestRunner


class QqLoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('this is setupclass')

    @classmethod
    def tearDownClass(cls):
        print('this is teardowmclass')

    def setUp(self):
        print('this is setup')

    def tearDown(self):
        print('this is teardowm')

    def test_01(self):
        print('this is case01')

    def test_02(self):
        print('this is case02')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(QqLoginCase("test_01"))
    suite.addTest(QqLoginCase("test_02"))
    file_path = r"E:\github\Python\Appium\report\result.html"
    with open(file_path, "wb") as f:
        HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告如下', description='详细').run(suite)
