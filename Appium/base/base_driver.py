# coding = utf-8
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand


class Driver:
    def __init__(self):
        self.write_file = WriteUserCommand()

    def android_driver(self, i):
        devices = self.write_file.get_yaml_value('user_info_' + str(i), 'deviceName')
        port = self.write_file.get_yaml_value('user_info_' + str(i), 'port')
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": devices,
            "app": r"E:\apk\QQ.apk",
            "appWaitActivity": "com.tencent.mobileqq.activity.LoginActivity",
            # "waitActivity": "",
            "noReset": "True"
        }
        driver = webdriver.Remote("http://127.0.0.1:"+port+"/wd/hub", capabilities)
        time.sleep(5)
        return driver

    def ios_driver(self):
        pass

    # 如果设备是android 就getandroi_driver 如果是ios ...
    def get_driver(self):
        pass
