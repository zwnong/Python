# coding = utf-8
"""
@All-project: Study
@author: ZWNONG
@file: 生成二维码.py
@time: 2020-09-23 20:28:50
"""
from MyQR import myqr
import os


def d():
    os.system(r'adb shell am start -n com.tencent.mobileqq/com.tencent.mobileqq.activity.SplashActivity')


myqr.run(
    words=r'https://user.qzone.qq.com/948276961?source=aiostar',
    picture=None,
    level='H',
    colorized=True,
    save_name='123.png',

)
