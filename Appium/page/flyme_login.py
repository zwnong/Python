# coding = utf-8
from base.base import Base
from util.read_ini import ReadIni
from appium import webdriver


class FlyMe_Login(Base):

    readini = ReadIni()
    flyMeUserName = readini.get_value('flyMeUserName', 'settingsElements')
    flyMePassWord = readini.get_value('flyMePassWord', 'settingsElements')
    loginButton = readini.get_value('loginButton', 'settingsElements')
    finshButton = readini.get_value('finshButton', 'settingsElements')

    def userName_input(self, flyMeUserName):
        self.find_by_id(self.flyMeUserName).click()
        return self

    def password_input(self, flyMePassWord):
        self.find_by_id(self.flyMePassWord).click()
        return self

    def loginbutton_click(self, loginButton):
        self.find_by_idAdnText(self.loginButton).click()
        return self

    def finshbutton_click(self, finshButton):
        self.find_by_id(self.finshButton).click()
