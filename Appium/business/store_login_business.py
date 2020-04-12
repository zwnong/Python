# coding = utf-8
from handle.store_login_handle import StoreLoginHandle


class StoreLoginBusiness:
    def __init__(self, driver):
        self.store_login_handle = StoreLoginHandle(driver)

    def login_pass(self):
        self.store_login_handle.send_username('18778600955')
        self.store_login_handle.send_password('nzw18778600955')
        self.store_login_handle.click_loginbtn()

    def login_fail(self):
        self.store_login_handle.send_username('18778600955fail')
        self.store_login_handle.send_password('nzw18778600955')
        self.store_login_handle.click_loginbtn()
