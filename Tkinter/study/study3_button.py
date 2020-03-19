# coding utf-8

import tkinter

# 创建窗体
window = tkinter.Tk()
window.title('tools')
window.geometry('400x400+200+50')


def MethodName():
    print('------------------')


# 创建按钮
button1 = tkinter.Button(window,
                         text="按钮",
                         command=MethodName,  # 按钮的作用 = 传入方法的名字
                         width=10,
                         height=10
                         ).pack()

button2 = tkinter.Button(window,
                         text="按钮",
                         command=lambda: print('bbbbbb')
                         ).pack()

# 退出按钮
button3 = tkinter.Button(window,
                         text="退出",
                         command=window.quit()
                         ).pack()

window.mainloop()
