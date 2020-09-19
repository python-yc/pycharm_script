'''
题目：反向输出一个链表。

程序分析：无。
'''
if __name__ == '__main__':
    ptr = []
    for i in range(3):
        try:
            num = int(input("please in put a number:\n"))
        except ValueError:
            num = 100
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)


