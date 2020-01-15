# coding=utf-8

import time
import unittest
import uiautomator2 as u2
from appium import webdriver
import HTMLTestRunner


# 定义测试类,必须继承父类unittest.TestCase
class settings_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Z91QAEVQUA8PD",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            # "app": r"E:\\APK\\com.shoujiduoduo.wallpaper.apk",
            # "appWaitActivity": "com.shoujiduoduo.wallpaper.ui.SplashActivity",
            "noReset": "True"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)
        return cls.driver

    # 定义setUp()
    def setUp(self):
        print('用例开始前执行的')

    # 定义tearDown()
    def tearDown(self):
        print('用例结束执行的')
        self.driver.quit()

    # 编写测试用例 以"test_"开头
    def test_case01(self):
        """

        :return:
        """
        # 运营商列表
        # list定位，点击运营商网络
        elements = self.driver.find_elements_by_id('com.android.settings:id/title')
        elements[1].click()
        time.sleep(1)
        # 判断sim是否存在
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("中国移动")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.meizu.connectivitysettings:id/switchWidget").text("开启")').click()
        time.sleep(10)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.meizu.connectivitysettings:id/switchWidget").text("关闭")').click()
        self.assertTrue()


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite
    suite.addTest(settings_Test('test_case01'))
    # 定义测试报告的路径
    report_file = r'C:\Users\v-nongzhongwen\Desktop\Folder\html_file\report.html'
    file_result = open(report_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title='网络管理p1、p2测试报告', description='用例执行完成')
    runner.run(suite)
