"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。

程序分析：无
"""
while True:
    x = float(input("please input a number:\n"))
    print(x**2)
    if x**2 < 50:
        break

# 用这个方法看着比较舒服
def SQ(x):
    return x * x
print('如果输入的数字平方值小于50，程序停止运行。')
again = 1
while again:
    num = float(input('请输入一个数字：\n'))
    print('运算结果为：%d' %(SQ(num)))
    if SQ(num) < 50:
        again = False   # 0
    # 这个可以不要
    else:
        continue
