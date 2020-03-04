# coding = utf-8
import time
import unittest
from appium import webdriver
import HTMLTestRunner


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cap = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "Z91QGEW42223W",
            "appPackage": "com.android.settings",
            "appActivity": ".Settings",
            "noReset": "True"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)
        time.sleep(5)
        return cls.driver

    @classmethod
    def tearDownClass(cls):
        print('teardowmclass')

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')

    def test_01(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.android.settings:id/title").text("登录 Flyme 账号")').click()
        self.driver.find_element_by_id('com.meizu.account:id/edtAccount').clear()
        self.driver.find_element_by_id('com.meizu.account:id/edtAccount').send_keys('18778600955')
        self.driver.find_element_by_id('com.meizu.account:id/edtPwd').send_keys('nzw18778600955')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId('
                                                        '"com.meizu.account:id/btn_login").text("登录")').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.meizu.account:id/finishBtn').click()

    @staticmethod
    def get_suite():
        suite = unittest.TestSuite()
        suite.addTest(TestCase("test_01"))
        # 获取当前时间
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        runner = HTMLTestRunner.HTMLTestRunner()
        file_path = r'D:\Python\PageObject\report\report' + now + '.html'
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='settings测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = TestCase()
    run.get_suite()
