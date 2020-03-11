# coding = utf-8
import sys

from page.flyme_login_page import FlyMeLoginPage


class FlyMeLoginaPageHandle:
    def __init__(self, driver):
        self.flyme_login_page_handle = FlyMeLoginPage(driver)

    # 操作页面的元素

    def send_username(self, user):
        """
        输入用户名
        """
        self.flyme_login_page_handle.userName_element().send_keys(user)

    def username_clear(self):
        self.flyme_login_page_handle.userName_element().clear()

    def send_password(self, password):
        """
        输入密码
        """
        self.flyme_login_page_handle.password_element(password).click()

    def click_login_button(self):
        """
        点击登录
        """
        self.flyme_login_page_handle.finish_button_element().click()
