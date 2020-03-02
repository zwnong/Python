# coding=utf-8
import os
import time
import unittest
import random
import uiautomator2 as u2
from appium import webdriver
import HTMLTestRunner

from selenium.common.exceptions import NoSuchElementException


class SettingsCase(unittest.TestCase):
    def get_src(self):
        t = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        self.driver.get_screenshot_as_file(r'Image\scr' + t + '.jpg')

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
    def test_01(self):
        t = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.android.settings:id/title").text("运营商网络")').click()

        try:
            dataSwitch = self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId('
                                                                          '"com.meizu.connectivitysettings:id'
                                                                          '/switchWidget")')
            self.driver.get_screenshot_as_file(r'Image\scr' + t + '.jpg')
        except NoSuchElementException:
            print('寻找数据流量元素异常')
        else:
            if dataSwitch[0].text != '关闭':
                print('移动数据开关未找到或已经打开')
            else:
                dataSwitch[0].click()
                self.driver.get_screenshot_as_file(r'Image\scr' + t + '.jpg')

    # 调节自动锁屏时间 30m
    # @unittest.skip
    def test_02(self):
        t = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.android.settings:id/title").text("显示和亮度")').click()

        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        self.driver.swipe(x / 2, y / 10 * 9, x / 2, y / 7)
        time.sleep(0.5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"android:id/title").text("自动锁屏")').click()
        el = self.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("android:id/text1")')
        el[5].click()
        self.driver.get_screenshot_as_file(r'Image\scr' + t + '.jpg')

    # 更换主题
    def test_03(self):
        t = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # 点击 主题和壁纸
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.android.settings:id/title").text("主题和壁纸")').click()

        time.sleep(0.5)
        # 随机选择壁纸
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"android:id/title").text("壁纸")').click()
        self.driver.get_screenshot_as_file(r'Image\scr' + t + '.jpg')

        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        for i in range(2):
            self.driver.swipe(x * 0.8222, y * 0.3952, x * 0.2777, y * 0.392)

        self.driver.find_element_by_android_uiautomator('new UiSelector().text("显示全部")').click()
        self.driver.get_screenshot_as_file(r'Image\scr' + t + '.jpg')
        pic = self.driver.find_elements_by_class_name("android.widget.ImageView")
        randint_data = random.randrange(1, 10)
        print("第：" + str(randint_data - 1) + '张')
        pic[randint_data].click()
        self.driver.find_element_by_id("com.meizu.customizecenter:id/btn_apply_wallpaper").click()
        time.sleep(0.5)
        self.driver.get_screenshot_as_file(r'Image\scr' + t + '.jpg')
        self.driver.find_element_by_id("com.meizu.customizecenter:id/setting_both").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.meizu.customizecenter:id/btn_apply_wallpaper").text("确定")').click()
        time.sleep(2)
        self.driver.get_screenshot_as_file(r'Image\scr' + t + '.jpg')
        self.driver.press_keycode(3)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SettingsCase("test_01"))
    suite.addTest(SettingsCase("test_02"))
    suite.addTest(SettingsCase("test_03"))
    # 获取当前时间
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    runner = HTMLTestRunner.HTMLTestRunner()
    file_path = r'C:\Users\v-nongzhongwen\Desktop\Folder\html_file\settings_report' + now + '.html'
    with open(file_path, 'wb') as f:
        HTMLTestRunner.HTMLTestRunner(stream=f, title='settings测试报告', description='描述:').run(suite)
