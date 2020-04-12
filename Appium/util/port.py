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


if __name__ == '__main__':
    dos = Port()
    print(dos.port_is_used('4723'))
