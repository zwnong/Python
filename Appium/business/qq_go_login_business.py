# coding = utf-8

from handle.qq_go_login_handle import QqGoLoginHandle


class QqGoLoginBusiness:
    def __init__(self):
        self.qq_go_login_handle = QqGoLoginHandle()

    def go_login(self):
        self.qq_go_login_handle.click_go_login_btn()

    def qq_login_pass(self):
        self.qq_go_login_handle.send_username('849130403')
        self.qq_go_login_handle.send_password('nzw15007867627&*')
        self.qq_go_login_handle.click_login_btn()
