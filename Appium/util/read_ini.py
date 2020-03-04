# coding = utf-8

import configparser


# conf = configparser.ConfigParser()
# conf.read(r'D:\Git\Learnning-Python\Appium\config\settingsElements.ini', encoding='UTF-8')
# print(conf.get('settingsElements', 'FlymeAccount'))


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = r'D:\Git\Learnning-Python\Appium\config\settingsElements.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    def read_ini(self):
        conf = configparser.ConfigParser()
        conf.read(self.file_path, encoding='UTF-8')
        return conf

    # 通过传入key，获取value
    def get_value(self, key, section=None):
        value = self.data.get(section, key)
        return value


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value('netWork', 'settingsElements'))
