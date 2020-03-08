# coding = utf-8
import sys
sys.path.append('D:\git\Python\Appium')
from page.flyme_login_page import FlyMeLoginaPage

class FlyMeLoginaPageHandle:
    def __init__(self,):
        self.flyme_login_page_handle = FlyMeLoginPage(driver)
        
        
    # 操作页面的元素

    def send_username(self, user):
        '''
        输入用户名
        '''
        self.driver.flyme_login_page_handle.userName_element().send_keys(user)


    def send_password(self, password):
        '''
        输入密码
        '''
        self.driver.flyme_login_page_handle.password_element().send_keys(password)

    def click_loginbutton(self):
        '''
        点击登录
        '''
        self.driver.flyme_login_page_handle.loginbutton_element().click()
    
