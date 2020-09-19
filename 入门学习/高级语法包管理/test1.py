#coding:utf-8
def stu(name,age):
    '''
    帮助文档以三引号开始和结束，放在方法内首位
    这是文档的内容
    :param name: 学生的姓名
    :param age: 学生的年龄
    :return: 无返回值
    '''
    pass


help(stu)
print('*'*10)
print(stu.__doc__)

print('================')
a,b = 1,3
print(round(a/b))
#保留小数方法一：
print(round(a/b,2))

print(format(float(a)/float(b)))
#保留小数方法二：
print(format(float(a)/float(b),'.2f'))

#保留小数方法三：
print('%.2f' %(a/b))

import math
'''
      小数的不同显示包含多种， floor， trunc，round

      floor，把小数向下截断到它的下层，即小于小数的最大整数。并且对负数有效。

      math.floor(2.5)) # 2

      math.floor(-2.5)) # -3

      trunc, 真截断，真正的截断了小数，所以当小数大于0时，效果与floor相同

      math.trunc(2.5)) # 2

      math.trunc(-2.5)) # -2

      round，格式化一个小数，与小学数学中的约等类似。round是内置函数，不需要倒入。

      round(2.567)) # 3

      round(2.467)) # 2

      round(2.567, 2)) # 2.57
'''
print(math.trunc(3.5))
print(math.trunc(-3.5))
print(round(-3.5))

#属性的三种操作，1、读取；2、赋值；3、删除
class A():
    def __init__(self):
        self.name = "NoName"
        self.age = 0

a = A()
print(a.name)
a.name = "xiaoming"
print(a.name)
del a.name
#在jupyter上执行删除后，再去打印属性会报错
#print(a.name)

#Python3.x的版本中input接收的是字符串，想要数字使用int(input())
x = input('shuruzhengshu')
if isinstance(x,str):
    print('OK')
else:
    print('Wrong')




