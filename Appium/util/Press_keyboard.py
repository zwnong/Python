# coding = utf-8
import os
from util.read_ini import ReadIni


class PressKeyboard:
    def adb(self, x, y):
        adb = os.popen('adb shell input tap x y')
        return adb


if __name__ == '__main__':
    adb = PressKeyboard()
    print(adb.adb('76', '1570'))
