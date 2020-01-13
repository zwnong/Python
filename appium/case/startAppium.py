# coding:utf-8
import time
import uiautomator2 as u2
from appium import webdriver

'''
Greated on  2020-01-13
@author: zwnong
projret: 
'''


def get_driver():
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
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    time.sleep(10)
    return driver


# 获取屏幕的宽高
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 向左边滑动
def swipe_left():
    # [100,200]
    x1 = get_size()[0] / 10 * 9
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10
    driver.swipe(x1, y1, x, y1, 2000)


# 向右边滑动
def swipe_right():
    # [100,200]
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1, 2000)


# 向上滑动
def swipe_up():
    # [100,200]direction
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    y = get_size()[1] / 10
    driver.swipe(x1, y1, x1, y, 1000)


# 向下滑动
def swipe_down():
    # [100,200]
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10
    y = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)


def swipe_on(direction):
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_left()
    else:
        swipe_right()


def test_login_flyme():
    time.sleep(2)
    element = driver.find_elements_by_id('com.android.settings:id/title')
    element[0].click()
    time.sleep(1)
    driver.find_element_by_id('com.meizu.account:id/edtAccount').send_keys('16620367115')
    time.sleep(1)
    driver.find_element_by_id('com.meizu.account:id/edtPwd').send_keys('meizu@888')
    time.sleep(1)
    driver.find_element_by_id('com.meizu.account:id/btn_login').click()
    time.sleep(5)
    driver.find_element_by_id('com.meizu.account:id/finishBtn').click()
    time.sleep(1)


driver = get_driver()
time.sleep(2)
test_login_flyme()

driver.quit()
