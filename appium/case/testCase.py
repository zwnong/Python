# 1、设置编码utf-8，导入模块 import unittest
# coding:utf-8
# 2、注解：包括创建时间，创建人，项目名称

"""
Greated on  2020-01-13
@author: zwnong
projret:apps
"""
import time
import unittest
from appium import webdriver


# 3、定义测试类：
class Test(unittest.TestCase):
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
            "noReset": "true"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(10)

    # 4、定义setUp(),用于测试前的初始化工作，注意 入参为“self”
    def setUp(self):
        self.number = input('输入一个数字')
        self.number = int(self.number)

    # 5、定义tearDown(),用于用例执行后的善后工作，注意 入参为“self”
    def tearDown(self):
        print('测试结束')

        # 6、定义测试用例，以“test_”开头，注意 入参为“self”，使用unittest.TestCase下的各种断言

    def test_case01(self):
        print(self.number)
        self.assertEqual(self.number, 10, msg="您输入的不是10")

    def test_case02(self):
        print(self.number)
        self.assertEqual(self.number, 20, msg="您输入的不是20")

    # 7、跳过用例的方法
    @unittest.skip('暂时跳过用例3的测试')
    def test_Case03(self):
        print(self.number)
        self.assertEqual(self.number, 30, msg="你输入的不是30")


# 8、如果直接运行该文件（if __name__ == "__main__":）,则执行以下语句
#   unittest.main()会搜索该模块下所有已test开头的测试用例并执行他们
if __name__ == "__main__":
    unittest.main()
