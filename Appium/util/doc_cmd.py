# coding = utf-8

import os


class DosCmd:
    def excute_result_list(self, command):
        result = os.popen(command).readlines()
        result_list = []
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list


if __name__ == '__main__':
    dos = DosCmd()
    print(dos.excute_result_list('adb devices'))
