#coding:utf-8
#运行一般采用debug模式
import mokuai

#将mokuai这个包导入后，相当于将这个包里的所有代码复制到此处，且运行了一遍
#因此在mokuai这个包里的第一平级的print会直接被执行出来
#一般不写一级的print语句，避免每次导入都执行

stu = mokuai.Student("xiaoming",20)
stu.say()
mokuai.sayHello()
#help(mokuai.Student)
#help(mokuai)
#这个doc的形式不可以这样用help可以用
#mokuai.Student.__doc__

while True:
    try:
        x = int(input("请输入一个整数"))
    except ValueError as e:
        print(e)
        continue
    else:
        print("ok")
        print(x)
        break



