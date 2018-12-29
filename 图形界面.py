# 2018.12.16
# maxzjs
# -*- coding:utf-8 -*-
# 图形界面

# 导入Tkinter包所有内容
from tkinter import *

# 从Frame派生一个Application类，是所有widget的父容器：
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text="Hello World!")
        self.helloLabel.pack()
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.pack()


# 实例化，并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('hello world!')
# 主消息循环
app.mainloop()