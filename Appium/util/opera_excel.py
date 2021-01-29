# coding = utf-8
"""
@All-project: Appium
@author: ZWNONG
@file: opera_excel.py
@time: 2020-06-26 15:43:53
"""
import xlrd


# file_path = r'E:\github\Python\Appium\config\case.xlsx'
# # 读取文件  拿到整个表数据
# excel = xlrd.open_workbook(file_path)
# data = excel.sheets()[0]
# # 打印行数
# print(data.nrows)
# # 打印一个数值 以0为下标 第4行第5列
# print(data.cell(2, 5).value)
# # 读取excel
class OperaExcel:
    def __init__(self, file_path=None, i=None):
        if file_path is None:
            self.file_path = r'E:\github\Python\Appium\config\case.xlsx'
        else:
            self.file_path = file_path
        if i is None:
            i = 0
        self.excel = self.get_excel()
        self.data = self.get_sheets(i)

    def get_excel(self):
        """
        获取excel
        :return:
        """
        execl = xlrd.open_workbook(self.file_path)
        return execl

    def get_sheets(self, i):
        """
        获取sheets（表格）的内容 i 表示某个表格
        :param i:
        :return:
        """
        tables = self.excel.sheets()[i]
        return tables

    def get_lines(self):
        """
        获取sheets行数
        :return:s
        """
        lines = self.data.nrows
        return lines

    def get_cell(self, row, cell):
        """
        获取单元格的值
        :return:
        """
        data = self.data.cell(row, cell)
        return data


if __name__ == '__main__':
    test = OperaExcel()
    print(test.get_lines())
    print(test.get_cell(2, 5))
    print(test.get_cell(4, 6))
