"""
处理一个输入的简单数字，并返回出息每个数字的次数
"""
# 分析：要去除两段的空白，然后要去掉左边开始的数字0
n = " 012352 ".strip().lstrip('0')
print("这是一个{}位数".format(len(n)))

for i in range(len(n)):
    print("{}'s count = {}".format(n[i],n.count(n[i])))

for j in range(len(n)):
    m = n[-j-1]
    print(m,end='')
print()
print(n)

for i in range(5,0,-1):
    print(i)

a = [1,2,3,4,5,6]
print(a[1::2])
print("########")
print(a[::-1])
print(a)
########################
# 把变量定义在最前面，便于理解
num = ""
while True:
    num = input("Please input a integer number:").strip()
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Bad number")

count = [0] * 10

for i in range(10):
    count[i] = num.count(str(i))

for i in range(10):
    if count[i]:
        print(str(i)+':'+count[i])

lst = list(num)
lst.reverse()
print(lst)
