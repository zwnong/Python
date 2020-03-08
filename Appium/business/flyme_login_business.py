# coding = utf-8
import sys
sys.path.append('D:\git\Python\Appium')
from handle.login_handle import FlyMeLoginaPageHandle

class LoginBusiness:
    def __init__(self):
        self.flyme_login_page_handle = FlyMeLoginaPageHandle(driver)

    def flyme_login_pass(self):
        self.flyme_login_page_handle.send_username('18778600955')
        self.flyme_login_page_handle.send_password('nzw18778600955')
        self.flyme_login_page_handle.click_loginbutton()
