# coding = utf-8
import sys

from util.read_ini import ReadIni


class GetIniValue(ReadIni):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        value1 = read_ini.get_value(key)
        by = value1.split('>')[0]
        value_by = value1.split('>')[1]

        if value1 is not None:
            if by == 'id':
                return self.driver.find_element_by_id(value_by)

            elif by == 'className':
                return self.driver.find_element_by_class_name(value_by)

            else:
                return None
