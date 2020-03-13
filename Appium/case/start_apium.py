# coding = utf-8
import time
import unittest
from appium import webdriver


def get_driver():
    capabilities = {
        "platformName": "Android",
        # "automationName": "UiAutomator2",
        "deviceName": "Z81MAEWABDBM3",
        "app": "com.android.settings",
        "appWaitActivity": "com.android.settings.Settings",
        "noReset": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver


driver = get_driver()
driver.find_elements_by_id('com.android.settings:id/right_arrow')[0].click()
