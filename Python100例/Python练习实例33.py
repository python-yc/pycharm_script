"""
题目：按逗号分隔列表。

程序分析：无。
"""
a = [1,2,3]
for i in a:
    if i == a[-1]:
        print(i)
    else:
        print(i,end=',')

s1 = ','.join(str(n) for n in a)
print(s1)



