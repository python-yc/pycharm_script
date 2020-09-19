#coding:utf-8

class Teacher():
    name = "dana"
    age = 18

    #这个self可以换成其他变量，只是规范使用self
    def say(self):
        '''
        这是帮助文档，检验一下打印
        :return: None
        '''
        self.name = "yaona"
        self.age = 17
        print("my name is {0}".format(self.name))
        #注意观察这个打印的结果，这个年龄访问的是初始化的变量
        print("my age is {0}".format(__class__.age))

    #python3.5（次版本）不支持方法内无self的这种写法，jupyter支持
    #def sayAgain():
        #print("Hello")

    def sayAgain(s):
        print("my name is {0}".format(s.name))
        print("my age is {0}".format(s.age))

print((Teacher.name))
print(Teacher.__dict__)
print("*" * 10)
print(Teacher.say.__doc__)
t = Teacher()
t.say()
print("*" * 10)
t.sayAgain()

class A():
    name = "liuying"
    age = 18

    def __init__(self):
        self.name = "aaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbb"
    age = 90

a = A()
#此时，系统会默认把a作为第一个参数传入函数
a.say()
print("*" * 10)
#此时，self被a代替
A.say(a)
print(A.name)
print(a.name)
#同样可以把A作为参数传入
A.say(A)

#此时，传入的是类实例B，因为B具有name和age的属性，所以不会报错
A.say(B)

#以上代码，利用了鸭子模型。鸭子模型：看起来是，用起来也还差不多，就不关心其真正的情况










