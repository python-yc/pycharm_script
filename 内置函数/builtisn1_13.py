# -*- coding: utf-8 -*-
### 1、abs()函数返回数字的绝对值

print("1、以下是abs函数的案例值")
print(abs(-1.2))

### 2、all()函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
# 元素除了是 数字0、空、FALSE 外都算 TRUE
# 以下是 all() 方法的语法:
# all(iterable) 参数 iterable -- 元组或列表。

print("2、以下是all函数的案例值")
print(all(['a', 'b', 'c', '']), end=" ")
print(all(['a', 'b', 'c', 0]), end=" ")
print(all(['a', 'b', 'c', '0']), end=" ")
print(all(['a', 'b', 'c', 'd']), end=" ")
print(all('a'))

### 3、any()函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
# 元素除了是 数字0、空、FALSE 外都算 TRUE
# 以下是 any() 方法的语法:
# any(iterable) 参数 iterable -- 元组或列表。

print("3、以下是any函数的案例值")
print(any(['a', 'b', 'c', 0]), end=" ")
print(any(['a', 'b', 'c', '0']), end=" ")
print(any([0]))

### 4、ascii() 函数类似 repr() 函数, 返回一个表示对象的字符串,
# 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。
# 生成字符串类似 Python2 版本中 repr() 函数的返回值

print("4、以下是ascii函数的案例值")
print(ascii('a'))
print(ascii(5))
print(type(ascii(5)))

### 5、bin()函数
# 参数： 整数型，参数不可为空
# 将一个整数转化为一个二进制整数，并以字符串的类型返回

print("5、以下是bin函数的案例值")
# print(bin('5'))   # TypeError: 'str' object cannot be interpreted as an integer
print(bin(5))
print(type(bin(5)))

### 6、bool()函数
# 函数用于将给定参数转换为布尔类型，如果没有参数，返回 False
# 是int 的子类
print("6、以下是bool函数的案例值")
print(bool(0), end=" ")
print(bool(6), end=" ")
print(bool(False), end=" ")
print(bool(''), end=" ")
print(bool(' '))

### 7、bytes()函数
# 函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。
# 它是 bytearray 的不可变版本
'''
以下是 bytes 的语法:
class bytes([source[, encoding[, errors]]])
参数
如果 source 为整数，则返回一个长度为 source 的初始化数组；
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
如果没有输入任何参数，默认就是初始化数组为0个元素。
返回值
返回一个新的 bytes 对象。
将一个字符串转换成字节类型
'''

print("7、以下是bytes函数的案例值")
print(bytes('python',encoding='utf-8'))   #输出b'python'
print(bytes('张三',encoding='utf-8'))     #输出b'\xe5\xbc\xa0\xe4\xb8\x89'
print(bytes([1,2,3,4]))                   #输出b'\x01\x02\x03\x04'
print(bytes('hello','ascii'))             #输出b'hello'

### 8.callable()函数
# 判断对象是否可以被调用
print("8、以下是callable函数的案例值")

print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))

def fn(x):
    return x*x
print(callable(fn))

### 9、chr()函数
# 查看十进制数对应的ASCII码值
# 参数　可以是 10 进制也可以是 16 进制的形式的数字，数字范围为 0 到 1,114,111 (16 进制为0x10FFFF)
# 返回值是当前整数对应的 ASCII 字符
print("9、以下是chr函数的案例值")
print(chr(0x30))     #输出 0
print(type(chr(0x30)))     #输出 0
print(chr(97))       #输出 a
print(chr(8364))     #输出 €

### 10、classmethod()函数
# 修饰符对应的函数不需要实例化，不需要 self 参数，
# 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
# 无参数； 返回函数的类方法
print("10、以下是classmethod函数的案例值")
class Stud:
    num = 100
    def fn1(self):
        print('方法一')
    @classmethod
    def fn2(cls):
        print('方法二')   # 输出 方法二
        print(cls.num)    # 调用类的实例化对象
        print("*" * 10)
        print(Stud().fn1())     ## 这个执行结果有个None，不知道什么意思
        print("*" * 10)
        cls().fn1()       # 调用类的方法
        # fn1()       # 添加类方法后，不能这样调用

Stud.fn2()    # 不需要实例化  #输出 方法二
print('===='*10)
object=Stud()
object.fn1()  # 需要实例化 # 输出 方法一

### 11、complex()函数
# 用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数
# 如果第一个参数为字符串，则不需要指定第二个参数
# class complex([real[, imag]])
# 参数说明：
# real -- int, long, float或字符串；
# imag -- int, long, float；
# 返回一个复数。
print("11、以下是complex函数的案例值")
print(complex(1,2))          #输出  (1+2j)
print(complex(1))            #输出  (1+0j)
print(complex('2'))          #输出  (2+0j)
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
print(complex('2+3j'))       #输出  (2+3j)
print(complex(1.2,3.4))      #输出  (1.2+3.4j)

### 12、complie()函数
# 将字符串编译成python能识别或可以执行的代码，也可以将文字读成字符串再编译
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
print("12、以下是complie函数的案例值")
s="print('hello world')"
r=compile(s,'hello','exec')
print(r)

### 13、delattr()函数
"""
delattr函数用于删除属性
delattr(x,'foobar)相当于del x.foobar
语法：setattr(object,name)
参数：object--对象;name--必须是对象的属性
返回值：空
"""
print("13、以下是delattr函数的案例值")
class People:
    sex = '男'
    def __init__(self, name):
        self.name = name
    def peopleinfo(self):
        print('欢迎{}访问'.format(self.name))

delattr(People, 'sex')
print(People.__dict__)
s = People.__dict__
print(s.get('sex', None))
