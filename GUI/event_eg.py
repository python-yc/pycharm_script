# 事件简单的例子
import tkinter

def baseLabel(event):
    global baseFrame
    lb = tkinter.Label(baseFrame,text="谢谢点击")
    lb.pack()

# 画出程序的总框架
baseFrame = tkinter.Tk()

lb = tkinter.Label(baseFrame,text="模拟按钮")
# lable绑定相应的消息和处理函数
# 自动获取左键点击，并启动相应的处理函数，baseLable
lb.bind("<Button-1>",baseLabel)
lb.pack()

#启动消息循环
#到此，表示程序开始运行
baseFrame.mainloop()

