"""
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换
# 注意 在python3中直接除会得到小数，不是去除小数的整数
"""

l = [1,2,3,4,5,6]
length = len(l)
print(l)
x = int((length+1)/2)
for i in range(x):
    l[i],l[length-1-i] = l[length-1-i],l[i]
print(l)




