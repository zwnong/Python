# coding = utf-8
import sys

import time
import unittest
from appium import webdriver
import HTMLTestRunner


class TestFlyMeLoginFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "973QAFV33GVJN",
            "app": r"E:\APK\com.taobao.taobao.apk",
            "appWaitActivity": "'com.taobao.tao.welcome.Welcome",
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)
        return self.driver

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        self.driver.press_keycode(3)

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(TestFlyMeLoginFunc("test_01"))
        # 获取当前时间
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        runner = HTMLTestRunner.HTMLTestRunner()
        file_path = r'D:\Git\Python\Study\report\report' + now + '.html'
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = TestFlyMeLoginFunc()
    run.case_suite()
