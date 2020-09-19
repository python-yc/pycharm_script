import time
#这个是不被推荐的线程包：_thread
import _thread as thread

#这个主要是注意使用参数时的写法
#使用多线程
def loop1(in1):
    #ctime 得到当前时间
    print('Start loop 1 at :',time.ctime())
    #把参数打印出来
    print("我是参数：",in1)
    #睡眠多长时间，单位是：秒
    time.sleep(4)
    print('End loop 1 at :',time.ctime())

def loop2(in1,in2):
    #ctime 得到当前时间
    print('Start loop 2 at :',time.ctime())
    #把参数打印出来
    print("我是参数：",in1,"和参数:",in2)
    #睡眠多长时间，单位是：秒
    time.sleep(2)
    print('End loop 2 at :',time.ctime())

def main():
    print("Starting at:",time.ctime())
    #启动多线程的意思是用多线程去执行某个函数
    #启动多线程函数为start_new_thread
    #参数两个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元组
    #注意：如果函数只有一个参数，需要参数后有一个逗号，即代表是元组
    thread.start_new_thread(loop1,("xiaoming",))
    thread.start_new_thread(loop2,("王老大","hong"))
    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()
    #其实是有三个线程在运行，一个主线程，用于分配工作；另外两个是工作的线程
    #然后这个是等待所有工作线程工作完
    while True:
        time.sleep(1)



















