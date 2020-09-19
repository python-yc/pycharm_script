# 简单画布
import tkinter

baseFrame = tkinter.Tk()

cvs = tkinter.Canvas(baseFrame,width=300,height=200)
cvs.pack()

# 一条线需要两个点指明起始
# 参数数字的单位是px
cvs.create_line(22,23,160,180)
cvs.create_text(56,67,text="I love python")

baseFrame.mainloop()

