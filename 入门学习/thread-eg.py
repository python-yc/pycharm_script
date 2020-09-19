'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''

"""
import time
为使用多线程
def loop1():
    #ctime 得到当前时间
    print('Start loop 1 at :',time.ctime())
    #睡眠多长时间，单位是：秒
    time.sleep(4)
    print('End loop 1 at :',time.ctime())

def loop2():
    #ctime 得到当前时间
    print('Start loop 2 at :',time.ctime())
    #睡眠多长时间，单位是：秒
    time.sleep(2)
    print('End loop 2 at :',time.ctime())

def main():
    print("Starting at:",time.ctime())
    loop1()
    loop2()
    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()


这个程序运行的结果：
Starting at: Sat Mar  2 09:55:49 2019
Start loop 1 at : Sat Mar  2 09:55:49 2019
End loop 1 at : Sat Mar  2 09:55:53 2019
Start loop 2 at : Sat Mar  2 09:55:53 2019
End loop 2 at : Sat Mar  2 09:55:55 2019
All done at: Sat Mar  2 09:55:55 2019

"""

import time
#这个是不被推荐的线程包：_thread
import _thread as thread

#使用多线程
def loop1():
    #ctime 得到当前时间
    print('Start loop 1 at :',time.ctime())
    #睡眠多长时间，单位是：秒
    time.sleep(4)
    print('End loop 1 at :',time.ctime())

def loop2():
    #ctime 得到当前时间
    print('Start loop 2 at :',time.ctime())
    #睡眠多长时间，单位是：秒
    time.sleep(2)
    print('End loop 2 at :',time.ctime())

def main():
    print("Starting at:",time.ctime())
    #启动多线程的意思是用多线程去执行某个函数
    #启动多线程函数为start_new_thread
    #参数两个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元组
    #注意：如果函数只有一个参数，需要参数后有一个逗号，即代表是元组
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()
    #其实是有三个线程在运行，一个主线程，用于分配工作；另外两个是工作的线程
    #然后这个是等待所有工作线程工作完，否则会主线程结束，其他线程被强制结束，未执行完毕
    # while True:
    #     time.sleep(1)






