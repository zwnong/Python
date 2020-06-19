# coding = utf-8
import time
from appium import webdriver


class Driver:
    def android_driver(self):
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "127.0.0.1:21503",
            "app": r"E:\apk\QQ.apk",
            "appWaitActivity": "com.tencent.mobileqq.activity.LoginActivity",
            # "waitActivity": "",
            "noReset": "True"
        }
        driver = webdriver.Remote("http://127.0.0.1:4700/wd/hub", capabilities)
        time.sleep(5)
        return driver

    def ios_driver(self):
        pass

    # 如果设备是android 就getandroi_driver 如果是ios ...
    def get_driver(self):
        pass


if __name__ == '__main__':
    run = Driver()
    run.android_driver()
