# coding = utf-8
import HTMLTestRunner
import time
import unittest
from appium import webdriver


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        # 如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "127.0.0.1:21503",
            "app": r"E:\APK\meizustore.apk",
            # "appWaitActivity": "com.meizu.store.newhome.NewHomeActivity",
            "noReset": "True"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(6)
        return self.driver

    def tearDown(self):
        self.driver.quit()

    def test_01(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.flyme.meizu.store:id/nav_title").text("我的")').click()
        time.sleep(1)
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.flyme.meizu.store:id/person_item_describe").text("未登陆")').click()
        time.sleep(5)

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(TestCase("test_01"))
        # 获取当前时间
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        runner = HTMLTestRunner.HTMLTestRunner()
        file_path = r'E:\github\Python\Appium\report\report' + now + '.html'
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = TestCase()
    run.case_suite()
