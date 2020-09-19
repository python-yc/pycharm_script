"""
题目：一个5位数，判断它是不是回文数。
即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无
"""

a = int(input("请输入一个五位数的数字：\n"))
x = str(a)
flag = True
if 9999 < a <100000:
    for i in range(2):
        if x[i] != x[-i-1]:
            flag = False
            break

    if flag:
        print("%d 是一个回文数。" %a)
    else:
        print("%d 不是一个回文数。" %a)
else:
    print("wrong")


    