#coding:utf-8
class A():
    name = "Noname"
    age = 18
    def __getattr__(self,name):
        print("meiyouzhaodao")
        print(name)

a = A()
print(a.name)
#print(a.addr)

class Person():
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print("设置属性：{0}".format(name))
        #下面这句会出现死循环
        #self.name = value
        #此种情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(name,value)

p = Person()
print(p.__dict__)
#print(p.__name__)  #有问题这句
print("============")
print("============")
p.age = 18

#__gt__

class Student():
    def __init__(self,name):
        self._name = name

    def __gt__(self, obj):
        print("haha,{0} 会比 {1} 大吗？".format(self,obj))
        return self._name > obj._name
stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)
print("=================")

#三种方法的案例
class Person():
    #实例方法
    def eat(self):
        print(self)
        print("Eating.....")
    #类方法
    #类方法的第一个参数一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing.....")

    #静态方法
    #不需要用参数，第一个参数表示自身或者类
    def say():
        print("Saying......")

yueyue = Person()
yueyue.eat()
#实例方法
#类方法
Person.play()
yueyue.play()
#静态方法
Person.say()








