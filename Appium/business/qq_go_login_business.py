# coding = utf-8

from handle.qq_go_login_handle import QqGoLoginHandle


class QqGoLoginBusiness:
    def __init__(self):
        self.qq_go_login_handle = QqGoLoginHandle()

    def qq_go_login_pass(self):
        self.qq_go_login_handle.click_go_login_btn()
