# coding = utf-8

from page.qq_go_login_page import QqGoLoginPage


class QqGoLoginHandle:
    def __init__(self):
        self.qq_go_login_page = QqGoLoginPage()

    def click_go_login_btn(self):
        return self.qq_go_login_page.get_go_login_element().cilck()
