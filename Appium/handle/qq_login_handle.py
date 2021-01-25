# coding = utf-8
import sys

sys.path.append(r'E:\github\Python\Appium')
from page.qq_login_page import QQLoginPage


# 操作层
class QQLoginHandle:
    # 对page页面元素的操作
    def __init__(self, i):
        self.qq_login_page = QQLoginPage(i)

    def go_login(self):
        """
        点击到登陆界面按钮
        :return:
        """
        return self.qq_login_page.go_login_element().click()

    def send_username(self, user):
        """
        输入用户名
        :param user:
        :return:
        """
        return self.qq_login_page.get_username_element().send_keys(user)

    def send_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        return self.qq_login_page.get_password_element().send_keys(password)

    def click_loginbtn(self):
        """
        点击登录按钮
        :return:
        """
        return self.qq_login_page.get_login_btn().click()

    def click_dialogRightBtn(self):
        """
        点击同意
        :return:
        """
        return self.qq_login_page.get_dialogRightBtn_element().click()

    def click_dialogLeftBtn(self):
        """
        点击赞不同意
        :return:
        """
        self.qq_login_page.get_dialogLeftBtn_element().click()
        return self.qq_login_page.get_username_element().clear(), self.qq_login_page.get_password_element().clear()

    def login_fail_prompt(self):
        """
        返回登录失败弹框元素，用于用例判断
        :return:
        """
        return self.qq_login_page.login_fail_prompt()

    def click_login_fail_promptBtn(self):
        """
        点击登录失败弹框中的确定
        :return:
        """
        return self.qq_login_page.login_fail_promptBtn().click()
