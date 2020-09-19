'''
#未使用锁的写法
import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        sum += 1

def myMinu():
    global sum,loopSum
    for i in range(1,loopSum):
        sum -= 1

if __name__ == '__main__':
    print("Staring...{0}".format(sum))

    #开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd,args=())
    t2 = threading.Thread(target=myMinu,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done ... {0}".format(sum))
'''

import threading

sum = 0
loopSum = 1000000

#生成一个锁的实例
lock = threading.Lock()

def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        #使用锁
        lock.acquire()
        sum += 1
        #释放锁
        lock.release()

def myMinu():
    global sum,loopSum
    for i in range(1,loopSum):
        #使用锁
        lock.acquire()
        sum -= 1
        #释放锁
        lock.release()

if __name__ == '__main__':
    print("Staring...{0}".format(sum))

    #开始多线程的实例，看执行结果是否一样
    t1 = threading.Thread(target=myAdd,args=())
    t2 = threading.Thread(target=myMinu,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done ... {0}".format(sum))














