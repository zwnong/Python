# coding = utf-8
import HTMLTestRunner
import time
import unittest
from appium import webdriver
from base.basedriver import BaseDriver
from page.main_page import MainPage


class TestFlyMeLoginFunc(unittest.TestCase):

    def setUp(self):
        cap = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "973QAFV33GVJN",
            "appPackage": "com.android.settings",
            "appActivity": "com.android.settings.Settings",

            "resetKeyboard": True,
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
        time.sleep(5)
        return self.driver

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        mp = MainPage(self.driver)
        mp.login_flyme().userName_input('18778600955').password_input(
            'nzw18778600955').loginbutton_click().finshbutton_click()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestFlyMeLoginFunc("test_01"))
    # 获取当前时间
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    runner = HTMLTestRunner.HTMLTestRunner()
    file_path = r'D:\Git\Learnning-Python\Appium\report\report' + now + '.html'
    with open(file_path, 'wb') as f:
        HTMLTestRunner.HTMLTestRunner(stream=f, title='settings测试报告', description='描述:').run(suite)
