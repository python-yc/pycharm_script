"""
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。
"""
#方法一：
s = 0
for n in range(1,21):
    x = 1
    for i in range(1,n+1):
        x *= i
    s += x
print("1! + 2! + ... + 20! = {}".format(s))

#方法二：
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x+1):
        r *= i
    return r
s = sum(map(op,l))
print("1! + 2! + ... + 20! = %d" %s)
