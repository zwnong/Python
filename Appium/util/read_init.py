# coding = utf-8

import configparser


class ReadIni:
    def __init__(self):
        self.ini_path = r'D:\Git\Python\Appium\config\Element.ini'
        self.data = self.read_ini()

    # 读取ini文件的方法
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.ini_path)
        return read_ini

    # 通过传入key获取value
    def get_value(self, key, section=None):
        if section is None:
            section = 'login_element'
        try:
            value = self.data.get(section, key)
        except EOFError:
            value = None
        return value


if __name__ == '__main__':
    re = ReadIni()
    print(re.get_value('password', 'login_element'))
