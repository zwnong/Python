# coding = utf-8
"""
@project: Reptile
@author: ZWNONG
@file: app_windows.py
@time: 2020-07-07 09:50:09
"""
# 窗体实现
import os

import PIL  # 图像处理模块
import numpy
import time
import threading
import matplotlib.pyplot as plt  # 画图模块
from matplotlib.widgets import Button  # 按钮模块
import warnings  # 屏蔽广告


class RunMain:
    def __init__(self):
        self.figure = plt.figure()  # 创建一个空白的图形对象
        self.coor = []  # 保存选择位置的坐标
        self.ax = None  # 子视图变量
        self.isAuto = False  # 标记是否启动了自动模式

    def get_scr_image(self):
        os.system('adb shell screencap -p /sdcard/screen.png')
        os.system('adb pull /sdcard/screen.png image/screencap/screen.png')
        # 将打开的图片转换成多为数组并返回
        return numpy.array(PIL.Image.open('image/screencap/screen.png'))

    def on_click(self, event):
        """
        坐标轴点击事件，event用于获取点击坐标点
        coor用于报错单机的起始坐标点与结束的坐标点
        :param event:
        :return:
        """
        if self.isAuto is False:  # 判断在买要启动自动跳跃时
            if event.xdata is not None and event.xdata is not None:  # 判断获取的坐标点是否为空
                # 获取点击的坐标点并转换为float
                x = float(event.xdata)
                y = float(event.xdata)
                # 此次判断为了躲避重选与自动按钮的坐标
                if x > 70 and y > 70:
                    self.coor.append((x, y))
                    if len(self.coor) == 1:
                        print('选中起点')
                    else:
                        print('选中重点')
                    self.ax = self.figure.add_subplot(1, 1, 1)  # 添加一个子图，也就是绘制我们选择的点
                    self.ax.plot(x, y, 'r*')  # 绘制红色的*号
                    self.figure.canvas.draw()  # 重画
                    # 如果coor 列表长度等于2时，将起始位置和终点位置的坐标点传递过去，然后情况坐标点
                    if len(self.coor) == 2:
                        # 调用计算方法，将起始位置和终点位置的坐标点传递过去，然后情况坐标点
                        self.jump_to_next(self.coor.pop())
                        self.ax.clear()
                        # 通过线程进行更新
                        th = threading.Thread(target=self.update)
                        th.start()
            else:
                print('已开启自动模式')

    def jump_to_next(self, param):
        pass

    def update(self):
        pass

    def main(self):
        axes_image = plt.imshow(self.get_scr_image(), animated=True)  # 将获取的图片显示在主窗口上
        self.figure.canvas.mpl_connect('button_press_event', self.on_click)
        # 重选按钮
        reelect_button_position = plt.axes([0.79, 0.8, 0.1, 0.08])  # 重选按钮的位置大小
        m = numpy.array(PIL.Image.open('image/reelect.png'))  # 重选按钮图片
        Button(reelect_button_position, label='', image=m)
        # 自动按钮
        m1 = numpy.array(PIL.Image.open('image/auto.png'))  # 自动按钮图片
        auto_button_posotion = plt.axes([0.79, 0.7, 0.1, 0.08])  # 自动按钮位置大小
        Button(auto_button_posotion, label='', image=m1)
        plt.show()

    def warning(self):
        return warnings.filterwarnings('ignore')


if __name__ == '__main__':
    app = RunMain()
    app.warning()
    app.main()
