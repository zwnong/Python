# coding = utf-8
import time

from util.dos_cmd import DosCmd
from util.port import Port
import threading
from util.write_user_command import WriteUserCommand


# 获取真正的设备信息类
class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.clear_data = WriteUserCommand()
        self.device_list = self.get_device()
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
        """
        创建可用端口
        :param start_port:
        :return:
        """
        port = Port()
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        """
        启动appium    拼接 appium -p -bp -U
        :argument
        :return:
        """
        write_file = WriteUserCommand()
        command_list = []
        appium_port_list = self.create_port_list(4700)  # 传入start_port,生成p端口列表
        bootstrap_port_list = self.create_port_list(4900)  # 生成bp端口列表
        devices_list = self.device_list  # 获取设备信息列表
        # for i in range(len(devices_list)):
        # 拼接命令
        command = "appium -p " + str(appium_port_list[i]) + " -bp " + str(bootstrap_port_list[i]) + " -U " + str(
            devices_list[i]) + " --no-reset --session-override"
        # 把命令添加到command_list
        command_list.append(command)
        write_file.write_data(i, devices_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))
        # 返回拼接好的命令，后续只需要循环这些命令
        return command_list

    def start_server(self, i):
        """
        获取start_list  然后循环
        :return:
        """
        self.start_list = self.create_command_list(i)
        print(self.start_list)
        self.dos.excute_cmd(self.start_list[0])

    def kill_server(self):
        """
        查找：tasklist | find "node.exe"
        杀进程：taskkill -F -PID node.exe
        :return:
        """
        # 查找结果列表
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def main(self):
        """
        多线程启动服务
        :return:
        """
        self.kill_server()
        self.clear_data.clear_data()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start.start()

        time.sleep(10)


if __name__ == '__main__':
    server = Server()
    print(server.get_device())
    print(server.create_port_list(4700))
    server.main()
