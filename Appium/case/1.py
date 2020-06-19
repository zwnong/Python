# coding = utf-8
import os
import unittest
import HTMLTestRunner


class A1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('this is setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('this is tearDownClass')

    def setUp(self) -> None:
        print('this is setUp')

    def tearDown(self) -> None:
        print('this is tearDown')

    def test_01(self):
        print('this is case1')

    def test_02(self):
        print('this is case2')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(A1("test_01"))
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    # html报告文件路径
    report_abspath = 'E:\\github\\Python\\Appium\\report\\result.html'
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告,测试结果如下:', description='用例执行情况:')
    # 调用add_case函数返回值
    runner.run(suite)
    fp.close()
