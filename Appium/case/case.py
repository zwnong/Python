# coding = utf-8
"""
@All-project: applets
@author: ZWNONG
@file: swipe_view.py
@time: 2020-06-29 22:57:44
"""
# coding = utf-8
import HTMLTestRunner
import time
import unittest
from appium import webdriver


class SwipeViewYouCheYouHuo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        capabilities = {
            'platformName': 'Android',
            'fastReset': 'false',
            'deviceName': '127.0.0.1:21503',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'fullReset': 'false',
            'unicodeKeyboard': 'True',
            'resetKeyboard': 'True',
            'chromeOptions': {
                'androidProcess': 'com.tencent.mm:appbrand0'
            }
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(6)
        return cls.driver

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        self.driver.find_element_by_xpath()

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(SwipeViewYouCheYouHuo("test_01"))
        # 获取当前时间
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        runner = HTMLTestRunner.HTMLTestRunner()
        file_path = r'E:\github\Python\applets\report' + now + '.html'
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = SwipeViewYouCheYouHuo()
    run.case_suite()
