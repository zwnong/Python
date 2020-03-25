# coding = utf-8
import os
import tkinter

# 创建窗体
window = tkinter.Tk()
window.title('monkey')
window.geometry("400x250+200+50")

"""
1、获取输入框输入的包名
2、点击执行按钮
"""


def twopackage():
    result = os.popen('adb shell dumpsys window | findstr mCurrentFocus').readline()
    print(result)
    a = result.split('u0')[1]
    package_name = a.split('/')[0]
    print(package_name)
    package2 = entry.get()
    numb = entry1.get()

    os.popen('adb shell monkey -p ' + package_name + '-p ' + package2 + '-s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20 --pct-nav 10 --pct-majornav '
                                                                        '10 --throttle '
                                                                        '800 --monitor-native-crashes -v -v ' + numb + '>E:\log.txt')


def button_two():
    result = os.popen('adb shell dumpsys window | findstr mCurrentFocus').readline()
    print(result)
    a = result.split('u0')[1]
    package_name = a.split('/')[0]
    print(package_name)
    numb = entry1.get()
    print(numb)
    os.popen('adb shell monkey -p ' + package_name + ' -s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20 --pct-nav 10 --pct-majornav 10 --throttle '
                                                     '800 --monitor-native-crashes -v -v ' + numb + '>E:\log.txt')


# 封装button1的功能,执行adb shell monkey -p com.meizu.filemanager -s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20
# --pct-nav 10 --pct-majornav 10 --throttle 1000 --monitor-native-crashes -v -v 10000 > E:\monkeylog\camrea.txt
def fnc():
    package = entry.get()
    numb = entry1.get()
    os.popen('adb shell monkey -p ' + package + ' -s 1000 --pct-touch 35 --pct-motion 25 --pct-appswitch 20 --pct-nav 10 --pct-majornav 10 --throttle '
                                                '800 --monitor-native-crashes -v -v ' + numb + '>E:\log.txt')


def button_stop():
    result = os.popen('adb shell "ps -A |grep monkey').readline()
    print(result)
    a = result.split("futex_wait_queue_me")[0]
    b = a[13:19]
    print(b)
    os.popen('adb shell kill -9\t' + b)


# 输入包名提示
label = tkinter.Label(window, text="请输入包名", justify="left")
label.pack()

# 创建输入框
# 包名输入框
entry = tkinter.Entry(window)
entry.pack()

# 提示输入次数框
label = tkinter.Label(window, text="请输入随机点击次数", justify="left")
label.pack()

# 输入次数框
entry1 = tkinter.Entry(window)
entry1.pack()

# 创建按钮  需要输入包名和点击次数
button1 = tkinter.Button(window, text="运行", command=fnc, width=19, height=1)
button1.pack()

# 输入随机数，运行当前应用
button2 = tkinter.Button(window, text="输入次数 运行当前应用", command=button_two, width=19, height=1)
button2.pack()

# 运行当前包名和指定包名
button3 = tkinter.Button(window, text="执行当前应用和指定包名", command=twopackage, width=19, height=1)
button3.pack()

# 停止按钮
button_stop = tkinter.Button(window, text="停\n止", command=button_stop, fg="red", width=5, height=19)
button_stop.pack()

window.mainloop()
