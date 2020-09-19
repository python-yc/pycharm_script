"""
题目：利用条件运算符的嵌套来完成此题：
学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
60分以下的用C表示。

程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子
"""
#方法一：
score = int(input("input your score"))

if score >= 90:
    grade = 'A'
elif 60 <= score < 90:      #elif score>=60:
    grade = 'B'
else:
    grade = 'C'

print('%d 属于 %s'%(score,grade))




