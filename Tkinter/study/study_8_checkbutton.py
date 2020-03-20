# coding = utf-8
import tkinter

"""
CheckButton:多选框控件
"""

window = tkinter.Tk()
window.title('tools')
window.geometry('400x400+200+50')


def updata():
    message = ""
    if hobby1.get():
        message += "money\n"
    if hobby2.get():
        message += "power\n"
    if hobby3.get():
        message += "people\n"

    # 清空text中的内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)


# 要绑定的变量
hobby1 = tkinter.BooleanVar()

# 多选框
cheak1 = tkinter.Checkbutton(window, text="money", variable=hobby1, command=updata)
cheak1.pack()

hobby2 = tkinter.BooleanVar()
cheak2 = tkinter.Checkbutton(window, text="power", variable=hobby2, command=updata)
cheak2.pack()

hobby3 = tkinter.BooleanVar()
cheak3 = tkinter.Checkbutton(window, text="people", variable=hobby3, command=updata)
cheak3.pack()

text = tkinter.Text(window, width=50, height=5)
text.pack()

window.mainloop()
