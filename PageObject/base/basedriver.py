# coding - utf-8
import time

from appium import webdriver

"""
1
"""


class BaseDriver:
    def Android_driver(self):
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
