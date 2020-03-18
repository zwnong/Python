# coding = utf-8
import time
import unittest
from appium import webdriver


def get_driver():
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


driver = get_driver()
driver.tap([(500, 500)], 500)
