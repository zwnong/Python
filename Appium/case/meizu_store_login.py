# coding = utf-8
import HTMLTestRunner
import time
import unittest


class TestMeiZuStoreLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('this is setupclass')

    @classmethod
    def tearDownClass(cls):
        print('this is setupclass')

    def setUp(self):
        print('this is setup')

    def tearDown(self):
        print('this is teardowm')

    def test_01(self):
        pass

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(TestMeiZuStoreLogin("test_01"))
        # 获取当前时间
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        runner = HTMLTestRunner.HTMLTestRunner()
        file_path = r'E:\Appium\report\report' + now + '.html'
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = TestMeiZuStoreLogin()
    run.case_suite()
