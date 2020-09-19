"""
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
程序分析：先把图形分成两部分来看待，
前四行一个规律，后三行一个规律，利用双重for循环，
第一层控制行，第二层控制列。
程序源代码：
"""

'''
#习题答案：
from sys import stdout

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print()

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print()

'''
# 自己写的
row = int(input("Please input the rowNumber"))
#首先打菱形的上半部分
for i in range(1,row+1):
    for j in range(row-i):
        print(end=' ')
    for k in range(2*i-1):
        print('*',end='')
    print()

#下半部分
row = row - 1
for i in range(1,row+1):
    for j in range(i):
        print(end=' ')
    for k in range(2*(row-i+1)-1):
        print('*',end='')
    print()


