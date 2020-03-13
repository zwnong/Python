# coding = utf-8
import HTMLTestRunner
import time
import unittest
import uiautomator2


class testCase(unittest.TestCase):

    def setUp(self):
        self.d = uiautomator2.connect('Z81MAEWABDBM3')
        # self.d.app_start('com.meizu.filemanager')
        self.d.app_start('com.android.settings')

    def tearDown(self):
        self.d.app_stop("com.meizu.filemanager")

    def test_01(self):
        self.d(resourceId='com.meizu.filemanager:id/mz_action_overflow_button').click()
        time.sleep(1)
        self.d(resourceId='com.meizu.filemanager:id/title', text='设置').click()

    def test_02(self):
        self.d.xpath(
            '//*[@resource-id="com.android.settings:id/list"]/android.widget.LinearLayout['
            '1]/android.widget.LinearLayout[1]').click()
        self.d(resourceId="com.meizu.account:id/rl_account_layout").click()
        self.d.send_keys("18778600955", clear=True)
        self.d(resourceId="com.meizu.account:id/edtPwd").click()
        self.d.send_keys("nzw18778600955", clear=True)
        self.d(resourceId="com.meizu.account:id/pressAnimLayout").click()
        self.d(resourceId="com.meizu.account:id/finishBtn").click()

    def test_03(self):
        pass

    @staticmethod
    def case_suite():
        suite = unittest.TestSuite()
        suite.addTest(testCase("test_02"))
        # 获取当前时间
        now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
        # runner = unittest.TextTestRunner()
        # runner.run(suite)
        runner = HTMLTestRunner.HTMLTestRunner()
        file_path = r'D:\Git\Python\UiAutomator2\report\report' + now + '.html'
        with open(file_path, 'wb') as f:
            HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='描述:').run(suite)


if __name__ == '__main__':
    run = testCase()
    run.case_suite()
