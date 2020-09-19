#sorted 案例
'''
sorted的使用
    sorted(序列[,reverse=False])
        - 默认reverse为False，结果为正序排列，为True时结果为倒叙
'''
a = [2,64,9,5,4]
al = sorted(a,reverse=True)
print(a)
print(al)

astr = ['dana','Dana','jingjing','wangxiao',"daai"]
str1 = sorted(astr)
print(str1)

str2 = sorted(astr,key=str.lower)
print(str2)

print("zip函数的使用如下")
##补充：高级函数
    # zip - 把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(type(z))
print(z)
for i in z:
    print(i,end=' ')
print()
# 这样使用可以，却不能对z进行dict然后直接打印，如：b = dict(z) print(b) 这样与以下的操作有什么鬼发生啊，一个可以一个不可以
info = dict(zip(l1,l2))
print(info)

b = dict(z)
print(b)

print("\nenumerate函数的使用如下")
#enumerate与zip的功能比较像
#对可迭代对象里的每一个元素配上一个索引，然后索引和内容构成一个新的列表
#默认是从0开始，可以修改
l1 = [11,12,131,14,15]
em = enumerate(l1,start=100)
print(type(em))
l2 = [i for i in em]
#这个可以直接进行打印，zip、map、filter不可以，不太清楚什么鬼
print(l2)
print("=======collections模块的使用如下==========")
###namedtuple、deque################
######nametuple:是一个可命名的tuple类型
import collections
#help(collections.namedtuple)
#此处代表一个点坐标
Point = collections.namedtuple("Point",['x','y'])
p = Point(11,22)
print(p.x)
print(p[0])
#此处代表一个圆
Circle = collections.namedtuple("Circle",['x','y','r'])
c = Circle(100,150,50)
print(c)
print(type(c))
print("deque的使用和结果如下###########")
#比较方便的解决了频繁插入带来的效率问题
from collections import deque
q = deque(['a','b','c'])
print(q)

q.append('d')
print(q)

q.appendleft('x')
print(q)

print("defaultdict函数的使用如下##############################")
#当直接读取dict不存在的属性时，直接返回默认值
d1 = {"one":1,"two":2,"three":3}
#此处调用不存在的键时，会报错
print(d1['one'],'######')

from collections import defaultdict
#help(collections.defaultdict)
func = lambda: "小明"
d2 = defaultdict(func)
#这样在访问字典中不存在的键时，会返回默认值（此处调用func函数），
#不会进行报错停止执行
d2["one"] = 1
d2["two"] = 2
print(d2['one'])
print(d2['three'])
print(type(collections))
print(type(collections.defaultdict))

print("############Counter的介绍和结果如下#######")
# Counter
    #- 统计字符串个数
from collections import Counter
#为什么下面结果不把整体作为键值，而是以其中每一个字母作为一个键
#需要括号内容可为迭代
c = Counter("asklhfkasljdfhasfhuiafglafo")
print(c)

s = ["xiaoming",'love','love','love','ok','hello']
c = Counter(s)
print(c)


