# coding = utf-8
import os


def get_pid():
    result = os.popen('adb shell "ps -A |grep monkey').readline()
    print(result)
    a = result.split("futex_wait_queue_me")[0]
    b = a[13:19]
    print(b)




    # print(result)
    # a = result.split('u0')[1]
    # package_name = a.split('/')[0]
    # print(package_name)



get_pid()