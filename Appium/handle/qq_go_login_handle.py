# coding = utf-8

from page.qq_go_login_page import QqGoLoginPage


class QqGoLoginHandle:
    def __init__(self, i):
        self.qq_go_login_page = QqGoLoginPage(i)

    def click_go_login_btn(self):
        """
        点击去登录页面的按钮
        :return:
        """
        return self.qq_go_login_page.get_go_login_element().click()

