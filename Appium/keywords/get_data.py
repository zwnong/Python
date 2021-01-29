# coding = utf-8
"""
@All-project: Appium
@author: ZWNONG
@file: get_data.py
@time: 2020-06-28 09:33:19
"""
from util.opera_excel import OperaExcel


# 固定列 传入行号 获取值
class GetData:
    def __init__(self):
        self.opera_excel = OperaExcel()

    def get_case_lines(self):
        """
        获取行号，在opera_excel已经有相应的方法，但为了后续简洁  不需要在导入其他的包，创立此方法
        :return:
        """
        lines = self.opera_excel.get_lines()
        return lines

    def get_handle_step(self, row):
        """
        获取操作步骤里面的方法名字
        传入行号，获取预期，调用opera_excel.get_cell(),将列写死
        :param row:
        :return:
        """
        method_name = self.opera_excel.get_cell(row, 3)
        if method_name is None:
            return None
        return method_name

    def get_element_key(self, row):
        """
        获取操作元素
        :param row:
        :return:
        """
        element_key = self.opera_excel.get_cell(row, 4)
        if element_key is None:
            return None
        return element_key

    def get_handle_value(self, row):
        """
        获取操作元素值
        :param row:
        :return:
        """
        handle_value = self.opera_excel.get_cell(row, 5)
        if handle_value is None:
            return None
        return handle_value

    def get_expect_element(self, row):
        """
        获取预期结果
        :param row:
        :return:
        """
        expect_element = self.opera_excel.get_cell(row, 6)
        if expect_element == '':
            return None
        return expect_element

    def get_expect_handle_step(self, row):
        expect_handle_step = self.opera_excel.get_cell(row, 7)
        if expect_handle_step is None:
            return None
        return expect_handle_step

    def is_run(self, row):
        """
        获取是否执行
        :param row:
        :return:
        """
        is_run = self.opera_excel.get_cell(row, 8)
        if is_run == 'yes':
            return True
        else:
            return False


if __name__ == '__main__':
    test = GetData()
    print(test.is_run(1))
