# coding = utf-8
from util.get_element_by_ini import GetElementByIni
from base.base_driver import Driver


class QqGoLoginPage:
    def __init__(self):
        base_driver = Driver()
        self.driver = base_driver.android_driver()
        self.get_element_by_ini = GetElementByIni(self.driver)

    def get_go_login_element(self):
        """
        获取登录按钮元素信息
        :return:
        """
        return self.get_element_by_ini.get_element('go_login')

    def get_go_btn_register_element(self):
        """
        获取注册按钮元素信息
        :return:
        """
        return self.get_element_by_ini.get_element('btn_register')

    def get_username_element(self):
        """
        获取用户名元素
        :return:
        """
        return self.get_element_by_ini.get_element('username')

    def get_password_element(self):
        """
        获取密码元素
        :return:
        """
        return self.get_element_by_ini.get_element('password')

    def get_login_btn(self):
        """
        点击登录按钮
        :return:
        """
        return self.get_element_by_ini.get_element('loginbtn')
