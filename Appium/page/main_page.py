# coding = utf-8
from PageObject.base.base import Base
from PageObject.page.flyme_login import FlyMe_Login


class MainPage(Base):
    goLogin = 'new UiSelector().resourceId("com.android.settings:id/title").text("登录 Flyme 账号")'
    # finshButton = 'com.meizu.account:id/finishBtn'

    def login_flyme(self):
        self.find_by_idAdnText(self.goLogin).click()
        # self.find_by_id(self.finshButton).click()
        return FlyMe_Login(self.driver)
