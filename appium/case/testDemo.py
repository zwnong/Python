# coding=utf-8
import os
import time
import unittest
from HtmlTestRunner import HTMLTestRunner
import uiautomator2 as u2
from appium import webdriver


def get_driver():
    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Z91QAEVQUA8PD",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings",
        # "app": r"E:\\APK\\com.shoujiduoduo.wallpaper.apk",
        # "appWaitActivity": "com.shoujiduoduo.wallpaper.ui.SplashActivity",
        "noReset": "True"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    time.sleep(5)
    return driver


driver = get_driver()
driver.press_keycode(3)
# os.system('adb shell am start -n com.android.alarmclock/com.meizu.flyme.alarmclock.DeskClock')
# time.sleep(1)
os.system('adb shell am start -n com.meizu.filemanager/com.meizu.flyme.filemanager.activity.HomeActivity')
time.sleep(1)
driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.meizu.filemanager:id/favorite_text_view'
                                            '").text("全部文件")')
time.sleep(1)
driver.press_keycode(3)
driver.quit()
# time.sleep(1)
# os.system('adb shell am start -n com.android.email/com.android.email.activity.setup.AccountSetupSelectActivity')
# time.sleep(1)
# os.system('adb shell am start -n com.meizu.connectivitysettings/com.meizu.connectivitysettings.SubSettings')
# driver.find_element_by_android_uiautomator('new UiSelector().text)').click()
# time.sleep(1)
# driver.find_element_by_android_uiautomator('new UiSelector().text("运营商网络")').click()
# elements = driver.find_elements_by_id('com.android.settings:id/title')
# elements[1].click()
