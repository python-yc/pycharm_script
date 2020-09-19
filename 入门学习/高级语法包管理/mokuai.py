#coding:utf-8
#包含一个类
#一个sayhello函数
#一个打印语句


class Student():

    def __init__(self,name="NoName",age=18):
         self.name = name
         self.age = age

    def say(self):
         print("My name is {0}".format(self.name))

def sayHello():
    print("Hi,欢迎来到我的世界！")

#只有运行本身模块式执行这个打印，再被调用时不执行
#通过添加一个判断进行改变
#此判断语句建议作为程序入口，即第一句被执行的代码；这是编程习惯的问题
#例子看test01
if __name__ == '__main__':
    print("我是模块01啊，叫我干啥")








