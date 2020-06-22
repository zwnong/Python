# coding = utf-8

from page.qq_go_login_page import QqGoLoginPage


class QqGoLoginHandle:
    def __init__(self):
        self.qq_go_login_page = QqGoLoginPage()

    def click_go_login_btn(self):
        """
        点击去登录页面的按钮
        :return:
        """
        return self.qq_go_login_page.get_go_login_element().click()

    def send_username(self, username):
        """
        操作输入用户名
        :param username:
        :return:
        """
        return self.qq_go_login_page.get_username_element().send_keys(username)

    def send_password(self, password):
        """
        操作输入密码
        :return:
        """
        return self.qq_go_login_page.get_password_element().send_keys(password)

    def click_login_btn(self):
        """
        点击登录按钮
        :return:
        """
        return self.qq_go_login_page.get_login_btn().click()
