# coding - utf-8
import time

from appium import webdriver

"""
1
"""


class BaseDriver:
    def __init__(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub")

    def Android_driver(self):
        cap = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "973QAFV33GVJN",
            # 1973
            "appPackage": "com.android.settings",
            "appActivity": "com.android.settings.Settings",
            'resetKeyboard': True,
            "noReset": "True"
        }
        time.sleep(5)
        return self.driver
