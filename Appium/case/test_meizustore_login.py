# coding = utf-8
import HTMLTestRunner
import time
import unittest
from appium import webdriver
from util.get_element_by_ini import GetElementByIni


class testTaoBaoSuite01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "973QAFV33GVJN",
            "app": r"E:\APK\meizustore.apk",
            # "Package": "com.meizu.account",
            "appWaitActivity": "com.meizu.account.login.activity.GrantActivity",
            "noReset": "True"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(6)
        return cls.driver

    get_element = GetElementByIni(0)

    def setUp(self):
        pass

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        self.get_element.get_element('username').send_keys('18778600955')
        time.sleep(1)
        self.get_element.get_element('password').send_keys('nzw18778600955')
        time.sleep(1)
        self.get_element.get_element('btn_login').click()

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(testTaoBaoSuite01("test_01"))
        # 获取当前时间
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        runner = HTMLTestRunner.HTMLTestRunner()
        file_path = r'D:\Git\Python\Appium\resport\report' + now + '.html'
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = testTaoBaoSuite01()
    run.case_suite()
