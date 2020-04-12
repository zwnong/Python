# coding = utf-8
from util.get_element_by_ini import GetElementByIni
from base.base_driver import Driver


# 元素层
class StoreLoginPage:
    def __init__(self, driver):
        self.driver = Driver()
        self.get_element_by_ini = GetElementByIni(driver)

    # 登录页面的所以元素
    def get_username_element(self):
        """
        # 获取用户名元素信息
        :return:
        """
        return self.get_element_by_ini.get_element('username')

    def get_password_element(self):
        """
        # 获取密码元素信息
        :return:
        """
        return self.get_element_by_ini.get_element('password')

    def get_login_btn_element(self):
        """
        # 获取登录按钮元素信息
        :return:
        """
        return self.get_element_by_ini.get_element('login_btn')
