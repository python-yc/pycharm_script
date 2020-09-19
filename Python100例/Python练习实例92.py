'''
题目：时间函数举例2。

程序分析：无。
'''
if __name__ == '__main__':
    import time
    start = time.time()
    for i in range(3000):
        print(i,end=' ')
        if i % 500 == 0 : print()
    end = time.time()
    print()

    print(end - start)


