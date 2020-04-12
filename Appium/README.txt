PO模型：
1、读取配置文件：产出：read_ini.py
    使用configparser读取ini
    通过参数key获取value

2、封装定位信息：产出：get_element_by_ini.py
    通过传入key获取对应的元素信息 并且 判断定位方式，
    产出：get_element_by_ini.py

3、分层思想
    page：元素层
    handle：操作层
    business：业务层
    page层只获取页面元素返回给操作层 进行 click send_key 等操作  业务层只需要调用操作层对应的方法输入数据，即：编写测试用例

    封装page层
        产出：page.py  用于封装页面所以元素信息
    封装handle层
        产出：handle.py  用于封装页面元素信息的操作
    封装business层
        产出：business.py  根据handle层  编写测试用例（）


4、服务端设计
    设计思想
        获取设备信息， 根据设备数量生成对应数量且对应的端口号

    启动appium:
        appium -p 4726 -bp 4724 -U 127.0.0.1:21503

    -需要devicename:
        产出dos_cmd.py  用于执行cmd命令：模块os  os.popen().readlines()
        重构：产出server.py  获取真正的设备信息


    -需要port:  产出port.py
        根据设备列表数量生成可以用的端口：
            1:检测端口是否可用：netstat -ano | findstr 4323
                有结果的时候说明端口被占用 调用dos_cmd.py 执行cmd命令来判断 被占用为 True  没被占用为False

            2:生成可用端口：
    -需要bp






