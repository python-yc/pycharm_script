"""
题目：输出 9*9 乘法口诀表。

程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
"""
#coding:utf-8
for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print("%d * %d = %d" %(j,i,i*j),end='  ')
    print()









