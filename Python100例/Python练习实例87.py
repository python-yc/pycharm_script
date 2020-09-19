'''
题目：回答结果（结构体变量传递）。

程序分析：无。
'''
if __name__ == '__main__':
    class Student():
        x = 0
        c = 0
    def f(stu):
        stu.x = 20
        stu.c = 'c'
    a = Student()
    a.x = 3
    a.c = 'a'
    f(a)
    print(a.x,a.c)



