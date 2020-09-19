'''
题目：时间函数举例3。

程序分析：无。
'''
if __name__ == '__main__':
    import time
    start = time.clock()
    for i in range(1000000):
        pass
    end = time.clock()
    print('different is %6.3f' %(end - start))


