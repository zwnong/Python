# coding = utf-8
import os


def get_package_vlue():
    result = os.popen('adb shell dumpsys window | findstr mCurrentFocus').readline()
    s = result.split(':')[1]
    print(s)
    a = s.split('/')
    print(a)
    b = a[0]
    print(b)

get_package_vlue()