# coding = utf-8
import sys

sys.path.append(r'E:\github\Python\Appium')
from handle.qq_login_handle import QQLoginHandle


# 业务层
class QQLoginBusiness:
    def __init__(self, i):
        self.qq_login_handle = QQLoginHandle(i)

    def go_login(self):
        self.qq_login_handle.go_login()

    def login_pass(self):
        """
        登录成功
        :return:
        """
        self.qq_login_handle.send_username('849130403')
        self.qq_login_handle.send_password('nzw15007867627&*')
        self.qq_login_handle.click_loginbtn()
        self.qq_login_handle.click_login_fail_promptBtn()
        self.qq_login_handle.click_loginbtn()
        # 判断是否登录成功

    def login_fail(self):
        """
        登录失败:
        :return:
        """
        self.qq_login_handle.send_username('849130402')
        self.qq_login_handle.send_password('nzw18778600955&*')
        self.qq_login_handle.click_loginbtn()
        if self.qq_login_handle.login_fail_prompt():
            return False
        else:
            return True
