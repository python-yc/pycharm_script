#######################################################
## 流畅的python 目录中也有相关，包括nonlocal 的使用
##闭包概念：
##  1.前提是函数有嵌套
##  2.内层函数引用了外层函数的变量（包括参数）
##  3.外层函数 又把 内层函数 当做返回值进行返回
#######################################################
def atest():
    a = 10
    def atest2():
        print(a)

    return atest2

# 将内部函数赋值给新的变量
newFunc = atest()
# 新变量也就是一个函数，正常调用
# newFunc()
print(newFunc)

# 应用场景
# 参数位置与传入是时的顺序有关，如果，以下调换一下，传参位置也调换一下就可以了
def line_config(length,content):
    print("have exected")
    def line():
        print('-' * (length // 2) + content + '-' * (length // 2))
    return line

line1 = line_config(20,"闭包")
line1()
line1()
line1()
line2 = line_config(30,"xxx")
line2()
line2()
line2()

## 闭包的经典的坑
def btest():
    funcs = []
    for i in range(1,4):
        def btest2():
            print(i)
        funcs.append(btest2)
    return funcs

newFuncs = btest()
print(newFuncs)
newFuncs[0]()
newFuncs[1]()
newFuncs[2]()
'''
这不是想要的结果：
[<function btest.<locals>.btest2 at 0x00000000007DC0D0>, <function btest.<locals>.btest2 at 0x00000000007DC158>, <function btest.<locals>.btest2 at 0x00000000007DC1E0>]
3
3
3
对其进行修改
'''
def btest():
    funcs = []
    for i in range(1,4):
        def btest2(num):
            def inner():
                print(num)
            return inner
        funcs.append(btest2(i))
    return funcs

print("########")
# newFuncs = btest()[0]() # 警告，不要这样写
newFuncs = btest()
print(newFuncs)
newFuncs[0]()
newFuncs[1]()
newFuncs[2]()

