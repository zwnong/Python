# coding = utf-8
import tkinter

# 创建窗体
window = tkinter.Tk()
window.title('tools')
window.geometry("400x400+200+50")

"""
Entry:输入控件，用于显示简单的文本内容
"""

# 显示密文
entry1 = tkinter.Entry(window,
                       show="*",  # show="*" 可以表示驶入密码
                       )
entry1.pack()

# 绑定变量 写入值 取值 显示值
e = tkinter.Variable()  # 可变的
entry2 = tkinter.Entry(window,
                       textvariable=e  # e代表这个输入框对象
                       )
entry2.pack()
# 设置值
e.set("初始值")
# 取值
print(e.get())
print(entry2.get())
window.mainloop()
