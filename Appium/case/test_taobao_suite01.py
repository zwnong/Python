# coding = utf-8
import HTMLTestRunner
import time
import unittest
from appium import webdriver

'''

'''


class testTaoBaoSuite01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "973QAFV33GVJN",
            "app": r"E:\APK\com.taobao.taobao.apk",
            "appWaitActivity": "com.taobao.tao.homepage.MainActivity3",
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)
        return self.driver

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        search = self.driver.find_element_by_id('com.taobao.taobao:id/search_icon')
        time.sleep(1)
        search.click()
        time.sleep(1)
        search.clear()
        time.sleep(1)
        search.send_keys('书籍')
        time.sleep(1)
        self.driver.find_element_by_id('com.taobao.taobao:id/searchbtn').click()

        self.driver.press_keycode(3)

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(testTaoBaoSuite01("test_01"))
        # 获取当前时间
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        runner = HTMLTestRunner.HTMLTestRunner()
        file_path = r'D:\Git\Python\Study\report\report' + now + '.html'
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)

if __name__ == '__main__':
    run = testTaoBaoSuite01()
    run.case_suite()

