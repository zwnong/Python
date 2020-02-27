# coding=utf-8
import os
import time
import unittest
import random

import uiautomator2 as u2
from appium import webdriver
import HTMLTestRunner
import sys


class settingsCase(unittest.TestCase):

    def setUp(self):
        print('每条用例执行前执行的.启动.settings appActivity')
        cap = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Z91QGEW42223W",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
        time.sleep(5)
        return self.driver

    def tearDown(self):
        print('每条用例执行完成后执行的')
        # 按HOME键
        # self.driver.press_keycode(3)

    # 打开数据流量
    @unittest.skip
    def test_01(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.android.settings:id/title").text("运营商网络")').click()
        time.sleep(0.5)
        dataSwitch = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                                     '"com.meizu.connectivitysettings:id/switchWidget'
                                                                     '").text(''"开启")')

        # print(l.text)
        if dataSwitch == "开启":
            print('数据已开启')

        else:
            self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                            '"com.meizu.connectivitysettings:id/switchWidget").text('
                                                            '"关闭")').click()
            time.sleep(0.5)
        self.assertEqual(dataSwitch.text, "开启", msg='开启数据失败')
        # self.driver.press_keycode(3)

    # 调节自动锁屏时间 30
    @unittest.skip
    def test_02(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.android.settings:id/title").text("显示和亮度")').click()
        self.driver.swipe(500, 2000, 500, 1100)
        time.sleep(0.5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"android:id/title").text("自动锁屏")').click()
        el = self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("android:id/text1")')
        el[5].click()

    # 更换主题
    def test_03(self):
        # 点击 主题和壁纸
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.android.settings:id/title").text("主题和壁纸")').click()
        time.sleep(0.5)
        # 随机选择壁纸
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"android:id/title").text("壁纸")').click()

        for i in range(2):
            self.driver.swipe(888, 888, 300, 888)

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("显示全部")').click()
        pic = self.driver.find_elements_by_class_name("android.widget.ImageView")
        randint_data = random.randrange(1, 10)
        print("第：" + str(randint_data - 1) + '张')
        pic[randint_data].click()
        self.driver.find_element_by_id("com.meizu.customizecenter:id/btn_apply_wallpaper").click()
        self.driver.find_element_by_id("com.meizu.customizecenter:id/setting_both").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.meizu.customizecenter:id/btn_apply_wallpaper").text("确定")').click()
        time.sleep(2)
        self.driver.press_keycode(3)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(settingsCase("test_01"))
    suite.addTest(settingsCase("test_02"))
    suite.addTest(settingsCase("test_03"))
    # 获取当前时间
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    runner = HTMLTestRunner.HTMLTestRunner()
    file_path = r'C:\Users\v-nongzhongwen\Desktop\Folder\html_file\settings_report.html'
    with open(file_path, 'wb') as f:
        HTMLTestRunner.HTMLTestRunner(stream=f, title='settings测试报告', description='描述:').run(suite)
