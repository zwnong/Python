# coding = utf-8
"""
@project: Study
@author: ZWNONG
@file: 设计个性签名.py
@time: 2020-09-26 20:33:27
"""
from tkinter import *
import requests
import re
from PIL import ImageTk


def func():
    # 获取窗口输入的名字
    name = entry.get()
    print(name)
    data = {
        'word': name,
        'sizes': '60',
        'fonts': '1.ttf',
        'fontcolor': '# 000000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    url = r'http://uustv.com/'
    result = requests.post(url, data, timeout=5).content.decode('utf-8')
    print(result)
    pattern = r'<img src="(.*?)"/></div>'  # 非贪婪模式 匹配需求最少的签名背景图片
    img_path = re.findall(pattern, result)[0]
    img_url = url + img_path
    print(img_url)
    with open(f'{name}的签名照.gif', "wb") as f:
        f.write(requests.get(img_url).content)

    # 将图片展现在窗口上
    bm = ImageTk.PhotoImage(filr=f'{name}的签名照.gif')
    lable2 = Label(root, image=bm)
    lable2.bm = bm
    lable2.grid(row=3, columnspan=2)


root = Tk()
root.geometry('540x305')
root.title('个性签名设计')

label = Label(root, text='名字：', font=("宋体", 25), fg='red')
label.grid()

entry = Entry(root, font=("宋体", 25), fg='black')
entry.grid(row=0, column=1)

button = Button(root, text='签名设计', font=("宋体", 25), fg='blue', command=func)
button.grid(row=1, column=1)

mainloop()
