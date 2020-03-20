# coding = utf-8

import time
from appium import webdriver


class BaseDriver:
    def android_driver(self):
        # devices
        # port
        capabilities = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "deviceName": "973QAFV33GVJN",
            "app": r"E:\APK\com.taobao.taobao.apk",
            "appWaitActivity": "com.taobao.tao.homepage.MainActivity3",
            "noReset": "True"
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)
        return driver
