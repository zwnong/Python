# coding = utf-8
import time

from appium import webdriver


class Driver:
    def android_driver(self):
        capabilities = {
            "platformName": "Android",
            # "automationName": "UiAutomator2",
            "deviceName": "127.0.0.1:21503",
            "app": r"E:\apk\meizustore.apk",
            "appWaitActivity": "com.meizu.store.newhome.NewHomeActivity",
            "noReset": "true"
        }
        self.android_driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(5)
        return self.android_driver

    def ios_driver(self):
        pass
