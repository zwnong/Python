# coding = utf-8

"""
经常需要调用的元素定位方法
"""


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 使用id定位
    def find_by_id(self, ID):
        return self.driver.find_element_by_id(ID)

    # 使用uiau id定位
    def find_by_uiautomator(self, ID):
        return self.driver.find_element_by_android_uiautomator(ID)

    # 使用uiau id和text定位
    def find_by_idAdnText(self, idAndText):
        return self.driver.find_element_by_android_uiautomator(idAndText)
