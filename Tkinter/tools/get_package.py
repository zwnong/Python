# coding = utf-8
import os


def get_package_vlue():
    result = os.popen('adb shell dumpsys window | findstr mCurrentFocus').readline()
    print(result)
    a = result.split('u0')[1]
    package_name = a.split('/')[0]
    print(package_name)
get_package_vlue()