# coding = utf-8

import os

result = os.popen('adb devices').readline()

print(result)
