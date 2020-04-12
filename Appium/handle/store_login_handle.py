# coding = utf-8
from page.store_login_page import StoreLoginPage


# 操作层
class StoreLoginHandle:
    # 对page页面元素的操作

    def __init__(self, driver):
        self.store_login_page = StoreLoginPage(driver)

    # 输入用户名
    def send_username(self, user):
        self.store_login_page.get_username_element().send_keys(user)

    # 输入密码
    def send_password(self, password):
        self.store_login_page.get_username_element().send_keys(password)

    # 点击登录按钮
    def click_loginbtn(self):
        self.store_login_page.get_username_element().click()
