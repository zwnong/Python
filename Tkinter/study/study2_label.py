# coding = utf-8

import tkinter

window = tkinter.Tk()
window.title('tools')
window.geometry("400x400+200+50")

"""
Label:标签控件，可现实文本

# win:主窗体
# text:显示文本内容
# bg:背景颜色
# fg:字体
# font:字体
# width:
# height:
# wraplength:指定text文本中多宽之后 换行
# justify:设置换行后的对其方式
# anchor：位置 n北 e东 w西 s南 center居中  组合 ne东北方向
"""

label = tkinter.Label(window,
                      text="hello",
                      bg="pink", fg="red",
                      font=("黑体", 20),
                      width=20,
                      height=10,
                      wraplength=100,
                      justify="left",
                      anchor="center"
                      )

# 显示出来
label.pack()
window.mainloop()
