# coding = utf-8
import tkinter

# 创建窗体
window = tkinter.Tk()
window.title('tools')
window.geometry("400x400+200+50")

"""
text:文本控制，用于显示多行文本  带滚动条的text
"""

# 创建滚动条
scroll = tkinter.Scrollbar()

text = tkinter.Text(window, width=30, height=10)

# side表示放到窗体的那一侧， fill表示填充

scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

text.pack()

str1 = "成长本身就是一件极为痛苦的事，不仅是指当你知道自己错了而没有机会改正时的痛苦；还包括着你所要面对的一些痛苦，" \
       "分离，还有你必定要经历的一些蜕变等等。所有的这些加起来构成了你我的青春。　　那些青涩的回忆，那些天真烂漫的想法，" \
       "那些让你牵动心灵的话，那些让你落泪的年华，那些曾经如花般灿烂的笑颜，那些曾经流淌温暖的画面，那些曾经在你自卑的日子里赐给你无限的勇气的人，" \
       "那些在你得意的日子里陪你一起喜悦的人，那些让你知道这个世界上有许多值得你去珍惜的人…所有的这些铸成你我精彩的青春。" \
       "物是人非事事休，我看年华，欲语泪先流。　　惜春春去，只是无情绪。望秋秋来，几点梧桐雨。　　暖雨轻风初冻破，日高烟敛，" \
       "更看今日晴未。　　人生若只是初见，该多好！那样我就一定不会再奢求什么华丽的结局，让时光停滞在你我相遇的刹那，我便会伴着你们熟悉的脸孔睡得香甜。　　" \
       "人，终究要在挣扎中蜕变，最终羽化成蝶。并不是所有的成长都要承受离别聚散的苦楚；并不是所有的成长都伴随着一个人流泪，" \
       "然后戴好面具说我并不孤独。我想，既然坚信自己能够成为蝴蝶，那就该忍受住疼痛去咬破自己织的茧；既然坚信自己能够成为雄鹰，" \
       "那就该努力地扑腾翅膀！无论结局是好是坏，我亦不后悔！也许风雨过后并不一定就有彩虹，但你依然可以收获雨后天空的澄净！　　" \
       "其实，你我的青春都一样，只是你我选择了不一样的方式停靠，有的青春在阳光下绽放，而有的青春却选择在角落里盛开。你我的青春不需要任何祭奠。" \
       "也请别把人生都当作地狱。也不要虚度青春，虚度青春不是青春把我们遗忘，而是你我将它看得过于廉价。 "
text.insert(tkinter.INSERT, str1)
window.mainloop()
