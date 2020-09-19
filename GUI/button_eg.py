# button的案例

import tkinter

def showLable():
    global baseFrame
    # 在函数中定义了一个label
    #label的父组件是baseFrame
    lb = tkinter.Label(baseFrame,text="显示Label")
    # 给相应组件指定布局
    lb.pack()

baseFrame = tkinter.Tk()
# 生成一个按钮
# command参数指示，当按钮被按下的时候，执行那个函数
btn = tkinter.Button(baseFrame,text="Show Label",command=showLable)
# 给相应组件指定布局
btn.pack()
baseFrame.mainloop()



