# coding = utf-8
from util.get_element_by_ini import GetElementByIni


class MeiZuStoreLoginPage:
    def __init__(self):
        self.get_element_by_ini = GetElementByIni(self.driver)

    # 获取登录界面所有元素

    def get_username_element(self):
        """
        获取用户名元素信息
        :return:
        """
        return self.get_element_by_ini.get_element('username')
