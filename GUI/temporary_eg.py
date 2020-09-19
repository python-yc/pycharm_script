import tkinter

baseFrame = tkinter.Tk()

# 生成一个级联菜单
menubar = tkinter.Menu(baseFrame)

menubar.add_cascade(label='File')

emenu = tkinter.Menu(menubar)
for item in ['Copy','Paste','Cut']:
    emenu.add_separator()
    emenu.add_command(label=item)
menubar.add_cascade(label='Edit',menu=emenu)

baseFrame['menu'] = menubar

lb = tkinter.Label(baseFrame,text='hello')
lb.pack(side=tkinter.LEFT)

baseFrame.mainloop()

