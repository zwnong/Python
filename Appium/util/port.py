# coding = utf-8

from util.doc_cmd import DosCmd


class Port:
    def port_is_used(self, port_number):
        """
        检测端口是否被占用
        :return:
        """
        dos = DosCmd()
        command = 'netstat -aon | findstr ' + str(port_number)
        result = dos.excute_result_list(command)
        # print(result)
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag


if __name__ == '__main__':
    port = Port()
    print(port.port_is_used('4723'))
