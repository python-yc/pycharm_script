#encoding:utf-8

#lambda表达式的用法
#1.以lambda开头
#2.紧跟着一定的参数（如果有的话）
#3.参数后用冒号和表达式主题隔开
#4.只是一个表达式，所以没有return

#计算一个数字的100的倍数
stm = lambda x: 100 * x

print(stm(89))

print("高阶函数的使用如下")
#高阶函数：把函数作为参数使用的函数
#变量可以赋值
a = 100
b = a
#函数名称就是一个变量
def funA():
    print("In funA")

funB = funA
funB()
###以上代码得出的结论：
'''
函数名称是变量
funB和funA只是名称不同而已
既然函数名称是变量，则应该可以当做参数传入另一个函数
'''
####高阶函数举例#################
##funA是普通函数，返回值个传入数字的100倍数字
def funA(n):
    return n * 100
##再写一个函数，把传入参数乘以300倍，
def funB(n):
    return funA(n) * 3
print(funB(9))
print("这是一个高阶函数的例子")
def funC(n,f):
    #假定知道函数式把n扩大100倍
    return f(n) * 3
print(funC(9,funA))
#比较funC和funB，funC的写法要优于funB
#例子如下########
def funD(n):
    return  n * 10
#需求变更，需要把n放大30倍，此时funB只有改代码才能实现此功能
#但是使用funC可以传另外的函数，便于使用
print(funC(9,funD))
print("################系统高阶函数-map###############")
'''
    原意就是映射，即把集合或者列表的元素的每一个元素都按一定
规则记性操作，生成一个新的列表或者集合。
    map函数式系统提供的具有映射功能的函数，返回值是一个迭代对象
    map使用格式map(函数名，可迭代项)
    在pyth3中，map的返回值回事一个map类的值，如：<map object at 0x0000000000A04A90>
因此要想打印处内容，可以是使用for循环打印
'''
# 利用map实现一个列表都扩大10倍
l1 = [1,2,3,4,5]
def mulTen(n):
    return n * 10
l2 = map(mulTen,l1)
#可以这样打印一个换行符，然后一起打印两个值
print(l1, "\n" ,l2)
for i in l2:
    #这样打印就不会出现每个值都进行一次回车
    print(i,end=" ")
print("\n以下这样进行打印为什么会出现列表为空，百度一下")
#为空原因:这是一个可迭代对象，迭代结束就结束了，所以为空## 这个解释不是很懂
l3 = [i for i in l2]
print(l3)
print("reduce的使用如下#########")
'''
reduce 
原意是归并，缩减
把一个可迭代对象最后归并成一个结果
对于作为参数的函数要求：必须有两个参数，必须返回结果
reduce([1,2,3,4,5]) == f(f(f(f(1,2),3),4),5)
reduce 需要导入functools包
格式：reduce(函数,序列)
'''
from functools import reduce

#定义一个操作函数
#加入操作函数只是相加
def myAdd(x,y):
    return x + y
#对于列表[1,2,3,4,5]执行myAdd的reduce操作
rst = reduce(myAdd,[1,2,3,4,5])
print(rst)

print("filter函数的的使用和结果如下")
'''
- 过滤函数：对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
- 跟map相比较：
    - 相同：都对列表的每一个元素逐一操作
    - 不同：map会生成一个跟原来数据相对应的新的队列，filter
    不一定，只要符合条件的才会进入新的数据集合
- filter的使用：
    利用给定函数进行判断
    返回值一定是个布尔值
    格式：filter(f,data)，f是过滤函数，data是数据
'''
def isEven(a):
    return a % 2 == 0

l = [3,4,62,6,8,7,9,45,6,4,5,445,4656]
#与map同样返回一个类，不能直接打印出内容，请百度
rst = filter(isEven,l)
print(type(rst))
print(rst)
#打印问题这可以这样解决
print([x for x in rst])







