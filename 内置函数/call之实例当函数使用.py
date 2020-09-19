# -*- coding: utf-8 -*-
"""call的使用，实例当函数使用，触发__call__魔法函数"""

class PenFactory:
    def __init__(self, p_type):
        self.p_type = p_type

    def __call__(self,p_color):
        print("创建了一个{}类型的画笔，它是{}颜色。".format(self.p_type, p_color))


gangbiF = PenFactory("pen")
gangbiF("red")
gangbiF("yellow")

print("#" * 10)
qianbiF = PenFactory("pencil")
qianbiF("blue")
qianbiF("black")

