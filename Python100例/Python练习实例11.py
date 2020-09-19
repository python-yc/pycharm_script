"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月
的兔子总数为多少？

程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""
#coding:utf-8

f1 = 1
f2 = 1
for i in range(1,12):
    print('%12d %12d'%(f1,f2),)
    if (i%3==0):
        print()
    f1 = f1 + f2
    f2 = f1 + f2

# a = 0
# b = 1
# n = int(input("Please input a number!"))
# for i in range(n):
#     a,b = b,a+b
#     print(a,end=' ')
#     if i%6==0:
#         print()

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

