# coding = utf-8
import os
import time
import tkinter

# 创建窗体
window = tkinter.Tk()
window.title('monkey')
window.geometry("400x200+200+50")

"""
1、获取输入框输入的包名（判断是否为真）
2、点击执行按钮
"""


def get_package_vlue():
    result = os.popen('adb shell dumpsys window | findstr mCurrentFocus').readline()
    print(result)
    a = result.split('u0')[1]
    package_name = a.split('/')[0]
    print(package_name)
    numb = entry1.get()
    print(numb)
    os.popen('adb shell monkey -p ' + package_name + ' -s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20 --pct-nav 10 --pct-majornav 10 --throttle '
                                                     '600 --monitor-native-crashes -v -v ' + numb + '>E:\log.txt')


# 封装button1的功能,执行adb shell monkey -p com.meizu.filemanager -s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20
# --pct-nav 10 --pct-majornav 10 --throttle 1000 --monitor-native-crashes -v -v 10000 > E:\monkeylog\camrea.txt
def fnc():
    package = entry.get()
    numb = entry1.get()
    os.popen('adb shell monkey -p ' + package + ' -s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20 --pct-nav 10 --pct-majornav 10 --throttle '
                                                '600 --monitor-native-crashes -v -v ' + numb + '>E:\log.txt')


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

# 创建按钮  需要输入包名和点击次数
button1 = tkinter.Button(window, text="运行", command=fnc, width=19, height=1)
button1.pack()

# 输入随机数，运行当前应用
button2 = tkinter.Button(window, text="输入次数 运行当前应用", command=get_package_vlue, width=19, height=1)
button2.pack()

window.mainloop()
