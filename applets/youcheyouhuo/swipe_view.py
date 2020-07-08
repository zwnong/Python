# coding = utf-8
"""
@project: applets
@author: ZWNONG
@file: swipe_view.py
@time: 2020-06-29 22:57:44
"""
import HTMLTestRunner
import os
import time
import unittest
from appium import webdriver


class SwipeViewYouCheYouHuo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "127.0.0.1:21503",
            "app": r"E:\base.apk",
            "appWaitActivity": "ycyh.com.driver.activity.MainActivity",
            "noReset": "True"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(6)
        return cls.driver

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01(self):
        self.driver.find_element_by_id('ycyh.com.driver:id/guide4').click()

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(SwipeViewYouCheYouHuo("test_01"))
        file_path = r'E\:report\result.html'
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = SwipeViewYouCheYouHuo()
    run.case_suite()
