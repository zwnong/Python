# coding = utf-8
import linecache
import time

import uiautomator2 as u2

device = u2.connect('127.0.0.1:21503')
device_package_name = 'com.smile.gifmaker'
size = device.window_size()
str_size = str(size)
x = str_size.strip('()').split(',')[0]
y = str_size.strip('()').split(',')[1]


def doubleClick():
    """
    :param x: 桌标x百分比点击
    :param y: 坐标y百分比点击
    菜单resouId:com.smile.gifmaker:id/left_btn
    os.system('taskkill /F /IM adb.exe')
    :return:
    
    """
    print("running...")

    while True:
        try:
            device.double_click(int(x) / 10 * 9.2, int(y) / 10 * 7, 0.2)
            time.sleep(0.16)
        except EOFError:
            print('fail')


def sendkey():
    file_path = r'./text.txt'
    with open(file_path, 'r+') as f:
        lists = []
        for i in f:
            lists.append(i)
        it = iter(lists)
        for j in it:
            x = next(j)
            print(x)

    # # 首先获得Iterator对象:
    # it = iter([1, 2, 3, 4, 5])
    # # 循环:
    # while True:
    #     try:
    #         # 获得下一个值:
    #         x = next(it)
    #         print(x)
    #     except StopIteration:
    #         # 遇到StopIteration就退出循环
    #         break


doubleClick()
# sendkey()
