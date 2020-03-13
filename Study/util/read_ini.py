# coding = utf-8
import sys
import configparser


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = 'D:\Git\Python\Appium\config\LoginElememts.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        read = configparser.ConfigParser()
        read.read(self.file_path, encoding='utf-8')
        return read

    # 通过key获取对应的value
    def get_value(self, key, section=None):
        if section is None:
            section = 'login_elements'
        try:
            value = self.data.get(key, section)
        except EOFError:
            value = None
        return value


if __name__ == '__main__':
    a = ReadIni()
    print(a.get_value('flyme_username', 'login_elements'))
