#coding:utf-8
import pkg01.p01
pkg01.inInit()
print("===================")
#此处也证明直接导入包，其实只导入了__init__，所以p01未导入
stu = pkg01.Student(age=1,name="xiaoming")
stu.say()






