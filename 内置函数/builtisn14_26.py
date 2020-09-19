# -*- coding: utf-8 -*-
### 14、dict()函数
"""
dict() 函数用于创建一个字典。
语法 dict 语法：
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
参数说明：
**kwargs -- 关键字
mapping -- 元素的容器。
iterable -- 可迭代对象。
返回一个字典。
"""
print("14、以下是dict函数的案例值")
print(dict())       #创建一个空字典
dict1 = dict(a = 'a', b = 'b', t = 't' )    #传入关键字，构造字典
print(dict1)

dict2 = dict(zip(['one', 'two', 'three'], ['1', '2', '3'])) #映射函数方式构造字典
print(dict2)

dict3 = dict([('one', 1), ('two', 2), ['three', 3]])    #可迭代对象方式构造字典
print(dict3)

### 15、dir()函数
"""
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，
该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
dir 语法：dir([object])
参数说明：object -- 对象、变量、类型。
返回值:返回模块的属性列表
"""
print("15、以下是dir函数的案例值")
print("当前模块的属性列表:", dir())        #获得当前模块的属性列表
print("列表的方法:", dir([]))      #获得列表的方法
print("字符串的方法：", dir(str))  #获得字符串的方法
print("字典的方法:", dir(dict))      #获得字典的方法

def update_func(var):
    print("var 的内存地址：", id(var))
    var += 4

lst_1 = [1, 2, 3]
print(dir())

class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']

s = Shape()
print(dir(s))

### 16、divmod()函数
"""
divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
在 python 2.3 版本之前不允许处理复数。
函数语法:divmod(a, b)
参数说明：
a: 数字
b: 数字
"""
print("16、以下是divmod函数的案例值")
print(divmod(20,4))   #返回  (5, 0)
print(divmod(7,2))    #返回  (3, 1)
# print(divmod(1+2j,1+0.5j))    TypeError: can't take floor or mod of complex number.

### 17、enumerate()函数
"""
enumerate是翻译过来是枚举的意思，看下它的方法原型：
enumerate(sequence, start=0)，返回一个枚举对象。
sequence必须是序列或迭代器iterator，或者支持迭代的对象。
enumerate()返回对象的每个元素都是一个元组，
每个元组包括两个值，一个是计数，一个是sequence的值，
计数是从start开始的，start默认为0。
"""
print("17、以下是enumerate函数的案例值")
a = ['q', 'w', 'e', 'r']
c = enumerate(a)
for i in c:
    print(i)

print('#' * 20)
a = ['q', 'w', 'e', 'r']
c = enumerate(a, 2)
for i in c:
    print(i)

#创建一个空字典
b=dict()
#这里i表示的是索引，item表示的是它的值
for i,item in enumerate(a):
    b[i]=item
print(b)   #输出 {0: 'q', 1: 'w', 2: 'e', 3: 'r'}

for i,j in enumerate('abc'):
    print(i,j)

### 18、eval()函数
"""
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
语法:以下是 eval() 方法的语法:
eval(expression[, globals[, locals]])
参数:expression -- 表达式。
globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
返回值:返回表达式计算结果
"""
print("18、以下是eval函数的案例值")
x=7
print(eval('3*x'))        #返回 21
print(eval('pow(2,2)'))   #返回 4

#eval函数还可以实现list、dict、tuple与str之间的转化

#1.字符串转换成列表
a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
print(type(a))         #返回  <class 'str'>
b = eval(a)
print(type(b))         #返回  <class 'list'>
print(b)               #输出  [[1, 2], [3, 4], [5, 6], [7, 8], [9, 0]]
#2.字符串转换成字典
a = "{1: 'a', 2: 'b'}"
print(type(a))        #返回  <class 'str'>
b = eval(a)
print(type(b))        #返回  <class 'dict'>
print(b)              #输出  {1: 'a', 2: 'b'}
#3.字符串转换成元组
a = "([1,2], [3,4], [5,6], [7,8], (9,0))"
print(type(a))        #返回 <class 'str'>
b=eval(a)
print(type(b))        #返回 <class 'tuple'>
print(b)              #输出 ([1, 2], [3, 4], [5, 6], [7, 8], (9, 0))

### 19、exec()函数
"""
函数的作用：
动态执行python代码。也就是说exec可以执行复杂的python代码，而不像eval函数那样只能计算一个表达式的值。
exec(source, globals=None, locals=None, /)
source：必选参数，表示需要被指定的python代码。它必须是字符串或code对象。如果source是一个字符串，该字符串会先被解析为一组python语句，然后执行。如果source是一个code对象，那么它只是被简单的执行。
返回值：
exec函数的返回值永远为None。

eval()函数和exec()函数的区别：
eval()函数只能计算单个表达式的值，而exec()函数可以动态运行代码段。
eval()函数可以有返回值，而exec()函数返回值永远为None
"""
print("19、以下是exec函数的案例值")
x = 10
def func():
    y = 20
    a = exec("x + y")
    print("a:", a)          #输出 a: None
    b = exec("x + y", {"x": 1, "y":2})
    print("b:", b)          #输出 b: None
    c = exec("x+y", {"x": 1, "y": 2}, {"y": 3, "z": 4})
    print("c:", c)  # 输出  c: None
    d = exec("print(x,y)")
    print("d:", d)  # 输出  d: None
func()

print('#' * 20)
x = 10
expr = """
z = 30
sum = x + y + z   #一大包代码
print(sum)
"""

def func():
    y = 20
    exec(expr)   #10+20+30       输出60
    exec(expr,{'x':1,'y':2}) #30+1+2         输出 33
    exec(expr,{'x':1,'y':2},{'y':3,'z':4}) #30+1+3，x是定义全局变量1，y是局部变量  输出34

func()

### 20、filter()函数
"""
filter() 函数是一个对于可迭代对象的过滤器，过滤掉不符合条件的元素，
返回的是一个迭代器，如果要转换为列表，可以使用 list() 来转换。
该函数接收两个参数，第一个为函数的引用或者None，第二个为可迭代对象，
可迭代对象中的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到迭代器中
"""
print("20、以下是filter函数的案例值")
my_list=[1,2,'',3,4,'6',' ']
new_list=list(filter(None,my_list))
print(new_list)

def is_oushu(x):
    return x%2==0
new_list=list(filter(is_oushu,list(range(1,11))))
print(new_list)

a=[1,2,3,4,5,6,2,2,2,]
print(list(filter(lambda x:x!=2,a)))

### 21、float()函数
"""
float() 函数用于将整数和字符串转换成浮点数。
float()方法语法：
class float([x])
参数:x -- 整数或字符串
返回浮点数
"""
print("21、以下是float函数的案例值")
print(float(1))            #输出  1.0
print(float(112.0))        #输出  112.0
print(float('123'))        #输出  123.0
print(float(True))         #输出  1.0
print(float(False))        #输出  0.0
#print(float('a'))          # ValueError: could not convert string to float: 'a'

### 22、format()函数
"""
自python2.6开始，新增了一种格式化字符串的函数str.format()，此函数可以快速处理各种字符串。
语法
它通过{}和:来代替%
"""
print("22、以下是format函数的案例值")
#通过位置
print ('{0},{1}'.format('chuhao',20))
#chuhao,20
print ('{},{}'.format('chuhao',20))
#chuhao,20
print ('{1},{0},{1}'.format('chuhao',20))
#20,chuhao,20
#通过关键字参数
print ('{name},{age}'.format(age=18,name='chuhao'))
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'This guy is {self.name},is {self.age} old'.format(self=self)

print (str(Person('chuhao',18)))       #This guy is chuhao,is 18 old

#通过映射 list
a_list = ['chuhao',20,'china']
print ('my name is {0[0]},from {0[2]},age is {0[1]}'.format(a_list))
#通过映射 dict
b_dict = {'name':'chuhao','age':20,'province':'shanxi'}
print ('my name is {name}, age is {age},from {province}'.format(**b_dict))

#填充与对齐
print ('{:>8}'.format('189'))
#     189
print ('{:0>8}'.format('189'))
#00000189
print ('{:a<8}'.format('189'))
#189aaaaa

#精度与类型f
#保留两位小数
print ('{:.2f}'.format(321.33345))      #321.33
#用来做金额的千位分隔符
print ('{:,}'.format(1234567890))       #1,234,567,890

#其他类型 主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制。
print ('{:b}'.format(18)) #二进制 10010
print ('{:d}'.format(18)) #十进制 18
print ('{:o}'.format(18)) #八进制 22
print ('{:x}'.format(18)) #十六进制12

### 23、frozenset()函数
"""
frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
frozenset() 函数语法：
class frozenset([iterable])
参数
iterable -- 可迭代的对象，比如列表、字典、元组等等。
返回值
返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合
"""
print("23、以下是frozenset函数的案例值")
a=frozenset(range(10))
print(a)
#输出  frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
b = frozenset('ltftyut1234')
print(b)

### 24、getattr()函数
"""
getattr()函数用于返回一个对象属性值
语法：getattr(object,name,default)
参数：
object--对象
name--字符串，对象属性
default--默认返回值，如果不提供该参数，在没有对应属性时，将触发AttributeError。
返回值：返回对象属性值
"""
print("24、以下是getattr函数的案例值")
class People():
    sex='男'
    def __init__(self,name):
        self.name=name
    def peopleinfo(self):
        print('欢迎%s访问'%self.name)

obj=getattr(People,'sex')
print(obj)       #返回值  男

### 25、globals()函数
"""
globals() 函数会以字典类型返回当前位置的全部全局变量。
globals() 函数语法：
参数:无
返回值:返回全局变量的字典
"""
print("25、以下是globals函数的案例值")
a='ltftyut1234'
print(globals()) # globals 函数返回一个全局变量的字典，包括所有导入的变量。

def zero_promo():
    return 0

def one_promo():
    return 1

def two_promo():
    return 2

def hello():
    print("Hello")

if __name__ == '__main__':
    promos = [name for name in globals() if name.endswith("_promo")]
    print(promos)   #输出 ['zero_promo', 'one_promo', 'two_promo']

    promos = [globals()[name] for name in globals() if name.endswith("_promo")]
    print(promos)
    print(promos[0]())

### 26、hasattr()函数
"""
hasattr()函数用于判断是否包含对应的属性
hasattr(object,name)
参数：
object--对象
name--字符串，属性名
返回值：如果对象有该属性返回True，否则返回False
"""
print("26、以下是hasattr函数的案例值")
class People():
    sex='男'
    def __init__(self,name):
        self.name=name
    def peopleinfo(self):
        print('欢迎%s访问'%self.name)

obj=People('zhangsan')
print(hasattr(People,'sex'))    #输出 True
print('sex'in People.__dict__)  #输出 True

print(hasattr(obj,'peopleinfo'))  #输出 True

