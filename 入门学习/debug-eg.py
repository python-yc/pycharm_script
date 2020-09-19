#encoding:utf-8
def SayHello(name):
    print("Hello,{0}".format(name))
    print("Done......")

"""
#pycharm调试
- run/debug模式
- 断点：程序的某一行，程序在debug模式下，遇到断点就会暂停
    - 代码与行号之间的空白处，点击左键即可添加断点

"""
if __name__=='__main__':
    print("*"*10)
    name = input("Please input your name:")
    SayHello(name=name)
    print("@"*10)








