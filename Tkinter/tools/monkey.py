# coding = utf-8
import os
import time
import tkinter

# 创建窗体
window = tkinter.Tk()
window.title('monkey')
window.geometry("400x400+200+50")

"""
1、获取输入框输入的包名（判断是否为真）
2、点击执行按钮
"""


# 封装button1的功能,执行adb shell monkey -p com.meizu.filemanager -s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20
# --pct-nav 10 --pct-majornav 10 --throttle 1000 --monitor-native-crashes -v -v 10000 > E:\monkeylog\camrea.txt
def fnc():
    os.popen('adb shell rm -rf sdcard/log1')
    time.sleep(1)
    os.popen('adb shell mkdir sdcard/log1')
    time.sleep(1)
    os.popen('adb shell touch sdcard/log1/log.txt')
    log = 'sdcard/log1/log.txt'

    package = entry.get()
    nub = entry1.get()

    os.popen('adb shell monkey -p ' + package + ' -s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20 --pct-nav 10 --pct-majornav 10 --throttle '
                                                '10 --monitor-native-crashes -v -v ' + str(nub) + log)


label = tkinter.Label(window, text="请输入包名", justify="left")
label.pack()

# 创建输入框
entry = tkinter.Entry(window)
entry.pack()

# 输入次数框
label = tkinter.Label(window, text="请输入随机点击次数", justify="left")
label.pack()

entry1 = tkinter.Entry(window)
entry1.pack()

# 创建按钮
button1 = tkinter.Button(window, text="运行", command=fnc, width=20, height=6)
button1.pack()

window.mainloop()
