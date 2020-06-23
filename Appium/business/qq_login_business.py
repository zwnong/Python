# coding = utf-8
from handle.qq_login_handle import QQLoginHandle


# 业务层
class QQLoginBusiness:
    def __init__(self, i):
        self.qq_login_handle = QQLoginHandle(i)

    # 操作登录界面的元素
    def login_pass(self):
        self.qq_login_handle.send_username('849130403')
        self.qq_login_handle.send_password('nzw15007867627&*')
        self.qq_login_handle.click_loginbtn()

    def login_fail(self):
        self.qq_login_handle.send_username('849130403')
        self.qq_login_handle.send_password('nzw18778600955')
        self.qq_login_handle.click_loginbtn()
