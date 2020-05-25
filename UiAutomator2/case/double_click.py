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

    while True:
        try:
            device.double_click(int(x) / 10 * 8.6, int(y) / 10 * 8, 0.2)
        except EOFError:
            print('fail')


def sendkey():
    file_path = r'./text.txt'
    with open(file_path, 'r+') as f:
        while True:
            for i in f:
                device(focused=True).send_keys(i)
                time.sleep(2)
                device.double_click(int(x) / 10 * 9.5, int(y) / 10 * 9.5, 0.1)


doubleClick()
