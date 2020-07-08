# coding = utf-8
"""
@project: Appium
@author: ZWNONG
@file: action_method.py
@time: 2020-06-28 09:10:49
"""
from base.base_driver import Driver
from util.get_element_by_ini import GetElementByIni


class ActionMethod:
    """
    关键字模型
    """

    def __init__(self):
        base_driver = Driver()
        self.driver = base_driver.android_driver(0)
        self.get_element_by_ini = GetElementByIni(self.driver)

    def input(self, *args):
        """
        输入值 element_key, value 用*args替代 *args是一个列表 element_key=*args[0] ; value=*args[1]
        :param element_key:
        :param value:
        :return:
        """
        element = self.get_element_by_ini.get_element(*args[0])
        if element is None:
            return '*args[0]', '元素未找到'
        element.send_keys(*args[1])

    def on_click(self, *args):
        """
        点击操作
        :param element_key:
        :param value:
        :return:
        """
        element = self.get_element_by_ini.get_element(*args[0])
        if element is None:
            return '*args[0]', '元素未找到'
        element.click()

    """
    滑动屏幕
    :return:
    """

    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动
    def swipe_left(self, *args):
        x1 = self.get_size()[0] / 10 * 9
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x, y1)

    # 想右滑动
    def swipe_reight(self, *args):
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x, y1)

    # 向上滑动
    def swipe_up(self, *args):
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        self.driver.swipe(x1, y1, x1, y)

    # 向下滑动
    def swipe_down(self, *args):
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1] / 10 * 9
        self.driver.swipe(x1, y1, x1, y)

    # 指定方向滑动
    def swip_on(self, direction, *args):
        if direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_down()
        elif direction == 'left':
            self.swipe_down()
        else:
            self.swipe_reight()

    def get_element(self, *args):
        """
        找元素的方法
        :param i:
        :return:
        """
        element = self.get_element_by_ini.get_element(*args[0])
        if element is None:
            return None
        return element
