"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，
插入后此元素之后的数，依次后移一个位置
"""
l = [2,6,9,10,15]
num = int(input("input a num:\n"))
length = len(l)
l.append(num)
for i in range(length):
    if l[length] < l[length-1]:
        l[length],l[length-1] = l[length-1],l[length]
        length -= 1
    else:
        break
print(l)






