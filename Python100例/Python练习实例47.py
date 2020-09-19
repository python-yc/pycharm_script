"""
题目：两个变量值互换。

程序分析：无
"""
a = 1
b = 2
print(a,',',b)
a,b = b,a
print(a,'<->',b)

def exchange(a,b):
    a, b = b, a
    return (a,b)
if __name__ == '__main__':
    x = 10
    y = 20
    print('x = {0},y = {1}'.format(x,y))
    x,y = exchange(x,y)
    print('x = %d,y = %d'% (x,y))

