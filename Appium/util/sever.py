# coding = utf-8

from util.dos_cmd import DosCmd
from util.port import Port


# 获取真正的设备信息类
class Server:
    def __init__(self):
        self.dos = DosCmd()
        # self.port = Port()

    def get_device(self):
        """
        #获取设备信息
        :return:
        """
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self, start_port):
        port = Port()
        port_list = port.create_port_list(start_port, self.get_device())
        return port_list

    def create_command_list(self):
        """
        启动appium    拼接 appium -p -bp -U
        :argument
        :return:
        """
        command_list = []
        appium_port_list = self.create_port_list(4700)  # 传入start_port,生成p端口列表
        bootstrap_port_list = self.create_port_list(4900)  # 生成bp端口列表
        devices_list = self.get_device()  # 获取设备信息列表
        for i in range(len(devices_list)):
            # 拼接命令
            command = "appium -p" + str(appium_port_list[i]) + " -bp" + str(bootstrap_port_list[i]) + " -U" + str(devices_list[i]) + " --no-reset --session-override"
            # 把命令添加到command_list
            command_list.append(command)
            # 返回拼接好的命令，后续只需要循环这些命令
            return command_list


if __name__ == '__main__':
    server = Server()
    print(server.get_device())
    print(server.create_port_list(4700))
    print(server.create_command_list())
