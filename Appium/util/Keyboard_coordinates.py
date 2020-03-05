# coding = utf-8
import os
from util.read_ini import ReadIni


class KeyboardCoordinates:

    def get_q(self):
        KeyboardLetter = ReadIni()
        q = KeyboardLetter.get_value('q', 'keyboardLetter')
        return q

    def get_w(self):
        KeyboardLetter = ReadIni()
        w = KeyboardLetter.get_value('q', 'keyboardLetter')
        return w


if __name__ == '__main__':
    adb = KeyboardCoordinates()
    print(adb.get_q())
