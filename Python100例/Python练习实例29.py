"""
题目：给一个不多于5位的正整数，
要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。
"""
# 方法一：
# 因为把数字当成一个字符串进行处理，便是解决
number = input("input a number")
count = 0
for i in number:
    count += 1
print("这是一个 {0} 位数的数字.".format(count))

print(number[::-1])

# 方法二：

x = int(input("请输入一个整数：\n"))
a = int(x / 10000)
b = int(x % 10000 /1000)
c = int(x % 1000 /100)
d = int(x % 100 /10)
e = int(x % 10)

if a != 0:
    print("5位数：",e,d,c,b,a)
elif b != 0:
    print("4位数：", e, d, c, b)
elif c != 0:
    print("3位数：", e, d, c)
elif d != 0:
    print("2位数：", e, d)
else:
    print("1位数：", e)