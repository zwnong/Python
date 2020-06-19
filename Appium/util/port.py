# coding = utf-8
from util.dos_cmd import DosCmd


class Port:
    def __init__(self):
        self.dos = DosCmd()

    def port_is_used(self, port_number):
        """
        #判断端口是否被调用
        :param port_number:
        :return:
        """
        command = 'netstat -ano | findstr ' + str(port_number)
        # 运行dos命令 判断端口是否被占用：如果有值（结果大于0）  表示被占用  结果返回True
        dos_result = self.dos.excute_cmd_result(command)
        if len(dos_result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, devices_list=None):
        """
        生成可用端口
        :param start_port:
        :param devices_list:
        :return:
        """
        port_list = []

        if devices_list is not None:
            while len(port_list) != len(devices_list):
                if not self.port_is_used(start_port):  # 如果端口不为True 即端口被占用
                    port_list.append(start_port)  # 将端口添加到port_list
                start_port = start_port + 1  # 因为添加端口之后，端口已经被占用，所以start_port就应该增加1
            return port_list
        else:
            print('生成可用端口失败')
            return None


if __name__ == '__main__':
    dos = Port()
    li = [1, 2, 3, 4, 5]
    print(dos.port_is_used('4700'))
    print(dos.create_port_list(4699, li))
