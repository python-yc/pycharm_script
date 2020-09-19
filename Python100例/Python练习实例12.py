"""
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
则表明此数不是素数，反之是素数
"""
#coding:utf-8
from math import sqrt
from sys import stdout
count = 0
#采用第三方进行判断，优秀
leap = 1
for i in range(101,201):
    #除到平方根的书就可以了，但是由于数字不能判断，除到加1再开方即可
    k = int(sqrt(i+1))
    for j in range(2,k+1):
        if i%j == 0:
            leap = 0
            break
    if leap == 1:
        count += 1
        #添加一个标记，便于观察
        print(i,'---',count)
    leap = 1

print("Total: {0}".format(count))






