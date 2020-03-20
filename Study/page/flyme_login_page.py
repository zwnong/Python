# coding = utf-8
import sys

from util.get_element_value_by_ini import GetIniValue


class FlyMeLoginPage(GetIniValue):
    def __init__(self, driver):
        """
        获取登录页面元素信息
        """
        super().__init__(driver)
        self.get_by_ini = GetIniValue(self.driver)

    def userName_element(self, flyMeUserName):
        """
        获取登录页面用户名元素信息
        """
        return self.driver.get_by_ini.get_element(flyMeUserName)

    def password_element(self, flyMePassWord):
        """
        获取登录页面密码元素信息
        """
        return self.driver.get_by_ini.get_element(flyMePassWord)

    def login_button_element(self, loginButton):
        """
        获取登录页面登录按钮元素信息
        """
        return self.driver.get_by_ini.get_element(loginButton)

    def finish_button_element(self, finish_button):
        return self.driver.get_by_ini.get_element(finish_button)
