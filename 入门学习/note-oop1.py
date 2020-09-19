#coding:utf-8
'''
定义一个学生类，用来形容学生
注意类和方法的命名方式
'''
#定义一个空的类
class Student():
    #一个空类，pass代表直接跳过
    #此处必须有pass，否则报错，不允许无内容
    pass

#定义一个对象类
yucai = Student()

#定义一个类，用来描述听Python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"
    #注意函数内有self，但调用时无需传参
    def doHomework(self):
        print("I 在做作业")
        #推荐在函数末尾使用return语句
        return None

#print(PythonStudent.__dict__)
#print(help(PythonStudent))
print("===============")
#此时，PyhtonStudent为类实例
print(PythonStudent.name)
print(PythonStudent.age)
print("===============")
#实例化一个叫yueyue的学生，是一个具体的人，即为对象实例
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传进参数
yueyue.doHomework()
#对象实例后未赋值
print(yueyue.__dict__)
print("===============")
#如果为对象实例赋值，则首先使用对象的值
yueyue.name = "xiaoli"
yueyue.age = 20
print(yueyue.name)
print(yueyue.age)
print(PythonStudent.name)
#对象实例后赋值后的变化
print(yueyue.__dict__)





