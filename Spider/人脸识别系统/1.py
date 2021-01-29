# coding = utf-8
"""
@All-project: Spider
@author: ZWNONG
@file: 1.py
@time: 2020-07-18 19:48:02
"""
import os

import cv2


def get_photo():
    # 0 表示摄像头编号
    capture = cv2.VideoCapture(0)
    # 拍照 ret (表示真和假)：到底有没有数据
    while True:
        #  ret, frame = capture.read(a, b)  此时会 ret=a frame=b
        # 如果用一个变量来接收 他会给到全部 frame = capture.read(a, b)  frame = a, b
        ret, frame = capture.read()

        # 图片展示
        cv2.imshow("face", frame)
        # ord()是一个函数 与print()类似 设置退出条件 检查 键盘按下 ‘q’  os.getpid()获取系统进程编号 9表示强制退出
        if cv2.waitKey(1) == ord('q'):
            os.kill(os.getpid(), 9)
