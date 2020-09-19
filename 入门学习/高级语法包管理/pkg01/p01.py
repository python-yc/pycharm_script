class Student():
    def __init__(self,name="NoName",age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayHello():
    print("Hi,欢迎来到我的世界！")
if __name__ == '__main__':
    print("我是模块01啊，叫我干啥")
