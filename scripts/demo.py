# coding=utf-8
import os
import string
import subprocess
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# 实例化 创建窗口
window = tk.Tk()
# 窗口的名字
window.title('IMSTOOLS')
# 窗口长 * 宽
window.geometry('250x110')
# 标签




def get_pid():
    pid_list = os.popen('adb shell "ps -A |grep imsdatadaemon').readline()
    pid = (pid_list[10:20])
    return pid


on_click = False


def on_get():
    pid = get_pid()
    global on_click
    if on_click:
        on_click = True
        var.set(pid)
    else:
        on_click = False
        var.set(pid)


def kill():
    pid = get_pid()
    obj = os.popen('adb shell kill -9 '+pid)
    # tkinter.messagebox.showinfo(title=pid, message=pid+'killed')
    global on_click
    if on_click:
        on_click = True
        var.set(pid+'killed')
    else:
        on_click = False
        var.set(pid+'killed')
    '''shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
     # info = obj.communicate(("\n".join(cmds) + "\n").encode('utf-8'))
   # for item in info:
       #if item:
           # print(item.decode('gbk'))
    '''
var = tk.StringVar()
V = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2).pack()
L = tk.Button(window, text='get', bg='green', font=('Arial', 12), width=10, height=1, command=on_get).pack()
K = tk.Button(window, text='kill', bg='green', font=('Arial', 12), width=10, height=1, command=kill).pack()

window.mainloop()
