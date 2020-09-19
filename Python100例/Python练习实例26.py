"""
题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!
"""
def fact(n):
    sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n * fact(n - 1)
    return sum

print(fact(5))





