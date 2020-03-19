# coding = utf-8
import tkinter

# 创建窗体
window = tkinter.Tk()
window.title('tools')
window.geometry("400x400+200+50")

"""
点击按钮输出输入框的内容
"""


def showinfo():
    # 获取输入的内容
    entry.get()

entry = tkinter.Entry(window)
entry.pack()

button = tkinter.Button(window, text="取值", command=showinfo)
button.pack()

window.mainloop()
