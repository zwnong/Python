# coding = utf-8
from base.base import Base


class FlyMe_Login(Base):
    flyMeUserName = 'com.meizu.account:id/edtAccount'
    flyMePassWord = 'com.meizu.account:id/edtPwd'
    loginButton = 'new UiSelector().resourceId("com.meizu.account:id/btn_login").text("登录")'
    finshButton = 'com.meizu.account:id/finishBtn'

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
