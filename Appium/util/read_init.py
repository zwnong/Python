# coding = utf=8

import configparser


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = r'E:\Appium\config\Element.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path, encoding='utf-8')
        return read_ini

    # 传入key获取value
    def get_value(self, key, section=None):
        if section is None:
            section = 'store_login'
        try:
            value_element = self.data.get(section, key)
        except EOFError:
            value_element = None
        return value_element


if __name__ == '__main__':
    value = ReadIni()
    print(value.get_value('username', 'store_login'))
