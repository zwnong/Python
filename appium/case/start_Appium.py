# coding=utf-8

import os
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
            # "appPackage": "com.android.settings",
            # "appActivity": ".Settings",
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
        # self.driver.quit()

    # 编写测试用例 以"test_"开头
    # 启用禁用sim卡
    def testCase01(self):
        """

        :return:
        """
        # 运营商列表
        # list定位，点击运营商网络
        elements = self.driver.find_elements_by_id('com.android.settings:id/title')
        elements[1].click()
        time.sleep(1)
        # 第 0 个为卡一id
        sim_elements = self.driver.find_elements_by_id('com.meizu.connectivitysettings:id/arrow')
        sim_elements[0].click()

        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("中国移动")').click()
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().resourceId("com.meizu.connectivitysettings:id/switchWidget").text("开启")').click()
        # time.sleep(10)
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiSelector().resourceId("com.meizu.connectivitysettings:id/switchWidget").text("关闭")').click()
        # self.assertTrue()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("android:id/title").text("启用")').click()
        time.sleep(1)
        # self.assertEqual(, '开启')

    # 编辑SIM卡名称
    def testCase02(self):
        # 需要先启动对应的activity
        # 按home健的值 3
        self.driver.press_keycode(3)
        time.sleep(1)
        os.system('adb shell am start -n com.meizu.connectivitysettings/com.meizu.connectivitysettings.SubSettings')
        time.sleep(1)
        # self.driver.start_activity('com.meizu.connectivitysettings/com.meizu.connectivitysettings.SubSettings')
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("android:id/title").text("编辑 SIM 卡名称")').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("android:id/edit").text("中国移动")').send_keys("中国联通")
        time.sleep(1)
        self.driver.find_element_by_id('android:id/button1').click()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(settings_Test('testCase01'))
    suite.addTest(settings_Test('testCase02'))
    # 定义测试报告的路径
    file = r'C:\Users\v-nongzhongwen\Desktop\Folder\html_file\report.html'
    fp = open(file, 'wb')
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='settings测试报告',description='123')
    runner.run(suite)
    fp.close()