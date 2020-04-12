# coding = utf-8
import time

from util.read_init import ReadIni


class GetElementByIni:
    # 这里开始第一次需要传入driver
    def __init__(self, driver):
        self.get_element_by_ini = ReadIni()
        self.driver = driver

    # 配置文件以 > 作为分割  左边为定位方式 右边为元素信息
    def get_element(self, key):
        value = self.get_element_by_ini.get_value(key)
        if value is not None:
            left_value = value.split('>')[0]
            right_value = value.split('>')[1]
            try:
                # 这里开始 判断>左边值 用对应的定位方式
                # 如 uid 为uiautomator的resourceId定位方式

                if left_value == 'uid':
                    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId(' + right_value + ')')
            except EOFError:
                # 如果有异常，则截图 或者做出对应操作
                now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
                self.driver.save_screenshot(r"D:\Git\Python\Appium\screenshot\shot" + now)
