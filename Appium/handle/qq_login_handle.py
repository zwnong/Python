# coding = utf-8
from page.qq_login_page import QQLoginPage


# 操作层
class QQLoginHandle:
    # 对page页面元素的操作
    def __init__(self, driver):
        self.qq_login_page = QQLoginPage(driver)

    # 输入用户名
    def send_username(self, user):
        self.qq_login_page.get_username_element().send_keys(user)

    # 输入密码
    def send_password(self, password):
        self.qq_login_page.get_password_element().send_keys(password)

    # 点击登录按钮
    def click_loginbtn(self):
        self.qq_login_page.get_login_btn_element().click()
