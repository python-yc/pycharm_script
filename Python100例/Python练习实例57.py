"""
题目：画图，学用line画直线。

程序分析：无。
"""
if __name__ == '__main__':
    from tkinter import *
    #import tkinter 这个导入的是个模块，上面导入的是模块内的所有

    canvas = Canvas(width=300,height=300,bg='green')
    canvas.pack(expand=YES,fill=BOTH)
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0,y0,x1,y1,width=1,fill='red')
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0,y0,x0,y1,fill='red')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()




