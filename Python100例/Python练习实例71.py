'''
题目：编写input()和output()函数输入，输出5个学生的数据记录。

程序分析：无。
'''
#!/usr/bin/python
# -*- coding:UTF-8 -*-

N = 3
#stu
#num : string
#name : string
#score[4] : list
student = []
for i in range(5):
    student.append(['','',[]])

def input_stu(stu):
    for i in range(N):
        stu[i][0] = input("please input student's num:\n")
        stu[i][1] = input("please input student's name:\n")
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))

def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' %(stu[i][0],stu[i][1]))
        for j in range(3):
            print('%-8d' %stu[i][2][j])

if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)