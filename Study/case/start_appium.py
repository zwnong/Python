# coding = utf-8
import os
import sys

import time
from appium import webdriver


def get_driver():
    apabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "973QAFV33GVJN",
        "app": r"E:\APK\com.taobao.taobao.apk",
        "appWaitActivity": "'com.taobao.tao.welcome.Welcome",
        "noReset": "True"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", apabilities)
    time.sleep(5)
    return driver


driver = get_driver()
# os.popen('adb shell am start -n com.flyme.meizu.store/com.meizu.store.newhome.NewHomeActivity')
# time.sleep(2)
# driver.lock()
# time.sleep(2)
# driver.unlock()
time.sleep(2)
driver.press_keycode(3)
