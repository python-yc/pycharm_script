'''
题目：读取7个数（1—50）的整数值，每读取一个值，
程序打印出该值个数的*。

程序分析：无。
'''
if __name__ == '__main__':
    n = 1
    while n <= 2:   # 7
        a = int(input('please input a number:\n'))
        while a < 1 and a > 50:
            a = int(input('please input a number:\n'))
        print(a*'*')
        n += 1


