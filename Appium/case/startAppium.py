# coding = utf-8
from base.base_driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from util.get_element_by_ini import GetElementByIni


def get_driver():
    driver = Driver()
    return driver.android_driver(0)


# 获取屏幕分辨率
def get_size():
    size = driver.get_window_size()
    width = size['width']
    height = size['height']
    return width, height


# 向左滑动
def swipe_left():
    x1 = get_size()[0] / 10 * 9
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10
    driver.swipe(x1, y1, x, y1)


# 想右滑动
def swipe_reight():
    x1 = get_size()[0] / 10
    y1 = get_size()[1] / 2
    x = get_size()[0] / 10 * 9
    driver.swipe(x1, y1, x, y1)


# 向上滑动
def swipe_up():
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10 * 9
    y = get_size()[1] / 10
    driver.swipe(x1, y1, x1, y)


# 想下滑动
def swipe_down():
    x1 = get_size()[0] / 2
    y1 = get_size()[1] / 10
    y = get_size()[1] / 10 * 9
    driver.swipe(x1, y1, x1, y)


# 指定方向滑动
def swip_on(direction):
    if direction == 'up':
        swipe_up()
    elif direction == 'down':
        swipe_down()
    elif direction == 'left':
        swipe_down()
    else:
        swipe_reight()


# id定位
def go_login():
    """
    # 显示等待  一般跟until() 或 until_not() 结合使用
    WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
    ——driver：WebDriver 的驱动程序(Ie, Firefox, Chrome 或远程)
    ——timeout：最长超时时间，默认以秒为单位
    ——poll_frequency：休眠时间的间隔（步长）时间，默认为 0.5 秒
    ——ignored_exceptions：超时后的异常信息，默认情况下抛 NoSuchElementException 异常
    :return:
    """
    # WebDriverWait(driver, 3, 1).until(lambda x: x.find_element_by_id(go_login_e)).click()
    # driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()


# 登录页面 id定位 输入账号密码(qq用户名没有id定位用class定位)
def login():
    WebDriverWait(driver, 3, 1).until(
        lambda driver: driver.find_element_by_xpath("//android.widget.EditText[@text='QQ号/手机号/邮箱' and @content-desc='请输入QQ号码或手机或邮箱']")).send_keys(
        '849130403')
    WebDriverWait(driver, 3, 1).until(lambda driver: driver.find_element_by_id('com.tencent.mobileqq:id/password')).send_keys('nzw15007867627&*')
    WebDriverWait(driver, 3, 1).until(lambda driver: driver.find_element_by_id('com.tencent.mobileqq:id/login')).click()


driver = get_driver()
go_login()
# login()
