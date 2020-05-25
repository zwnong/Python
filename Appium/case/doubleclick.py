# coding = utf-8
from appium import webdriver
from base.base_driver import Driver

file_path = './text.txt'
with open(file_path, 'r+') as f:
    line = f.readlines()
    it = iter(line)
    driver = Driver.android_driver()
    while True:
        try:
            x = next(it)
            if x == '/n':
                driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.smile.gifmaker:id/comment")'
                                                           '.text("说点什么...")').send_keys(x)
        except StopIteration:
            # 如果迭代器找不到元素则推出循环
            break

# def doubleClick():
#     driver = Driver.android_driver()
#     driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.smile.gifmaker:id/comment")'
#                                                '.text("说点什么...")').send_keys()
