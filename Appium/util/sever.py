# coding = utf-8

from util.dos_cmd import DosCmd


class Server:
    def __init__(self):
        self.dos = DosCmd()

    def get_device(self):
        """
        #获取设备信息
        :return:
        """
        device_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    device_list.append(devices_info[0])
            return device_list
        else:
            return None


if __name__ == '__main__':
    server = Server()
    print(server.get_device())
