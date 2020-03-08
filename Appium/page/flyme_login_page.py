# coding = utf-8
import sys
sys.path.append('D:\git\Python\Appium')
from util.get_ini_value import GetIniValue


class FlyMeLogin(GetIniValue):
    def __init__(self, driver):
        '''
        获取登录页面元素信息
        '''
        #self.get_by_ini = GetIniValue(driver)

    def userName_element(self):
        '''
        获取登录页面用户名元素信息
        '''
        return self.driver.get_by_ini.get_ini_element('flyMeUserName')

    def password_input(self, flyMePassWord):
        '''
        获取登录页面密码元素信息
        '''
        return self.driver.get_by_ini.get_ini_element('flyMePassWord')

    def loginbutton_click(self, loginButton):
        '''
        获取登录页面登录按钮元素信息
        '''
        return self.driver.get_by_ini.get_ini_element('loginButton')

    def finshbutton_click(self, finshButton):
        self.find_by_id(self.finshButton).click()
