"""
题目：求100之内的素数。

程序分析：无。
"""
for i in range(2,100):
    flag = 0
    for k in range(2,i):
        if i % k == 0:
            flag = 1
            break
    if flag:
        pass
    else:
        print(i,end=',')



