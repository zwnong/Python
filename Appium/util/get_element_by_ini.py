# coding = utf-8
import time

from util.read_init import ReadIni


class GetElementByIni:
    def __init__(self, driver):
        self.driver = driver

    # 封装》根据获取到元素判断对应的定位方式
    def get_element(self, key):
        read_ini = ReadIni()
        result_element = read_ini.get_value(key)
        if result_element is not None:
            left = result_element.split('>')[0]
            right = result_element.split('>')[1]
            try:
                # 如果ini文件中分割符左边=uid,则调用以下方法
                if left == 'uid':
                    self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId(' + right + ')')
            except EOFError:
                now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
                self.driver.save_screenshot(r"D:\Git\Python\Appium\screenshot\shot" + now)
