# coding = utf-8
from util.get_element_by_ini import GetElementByIni
from base.base_driver import Driver


# 元素层
class QQLoginPage:
    def __init__(self, i):
        base_driver = Driver()
        self.driver = base_driver.android_driver(i)
        self.get_element_by_ini = GetElementByIni(self.driver)

    def go_login_element(self):
        """
        获取到登录页面按钮的元素
        :return:
        """
        return self.get_element_by_ini.get_element('go_login')

    # 登录页面的所以元素
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

    def get_dialogRightBtn_element(self):
        """
        点击同意
        :return:
        """
        return self.get_element_by_ini.get_element('dialogRightBtn')

    def get_dialogLeftBtn_element(self):
        """
        赞不同意 按钮元素
        :return:
        """
        return self.get_element_by_ini.get_element('dialogLeftBtn')

    def login_fail_prompt(self):
        """
        登录失败弹框元素
        :return:
        """
        return self.get_element_by_ini.get_element('prompt')

    def login_fail_promptBtn(self):
        """
        登录失败弹框 确定 元素
        :return:
        """
        return self.get_element_by_ini.get_element('promptBtn')
