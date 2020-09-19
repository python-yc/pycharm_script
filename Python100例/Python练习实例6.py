"""
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），
又称黄金分割数列，指的是这样一个
数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
"""
#coding:utf-8
#方法一：
#n = int(input("Please input a integer"))
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
print(fib(10))

#方法二：
#采用递归方式
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))

#方法三：
#以列表的形式输出
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print(fib(10))



