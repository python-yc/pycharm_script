import time
#这个是不被推荐的线程包：_thread
import threading

#这个主要是注意使用参数时的写法
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

def loop3():
    #ctime 得到当前时间
    print('Start loop 3 at :',time.ctime())
    #睡眠多长时间，单位是：秒
    time.sleep(5)
    print('End loop 3 at :',time.ctime())

#与_thread真正的区别就在main()内
#main()才是真正执行干活的
def main():
    print("Starting at:",time.ctime())
    #启动多线程的意思是用多线程去执行某个函数
    #启动多线程函数为start_new_thread
    #参数两个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元组
    #注意：如果函数只有一个参数，需要参数后有一个逗号，即代表是元组
    t1 = threading.Thread(target=loop1,args=())
    #setName是给一个子线程设置一个名字
    t1.setName("THR_1")
    t1.start()

    t2 = threading.Thread(target=loop2,args=())
    t2.setName("THR_2")
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName("THR_3")
    t3.start()

    #预期3秒后thread2已经自动结束
    time.sleep(3)
    #enumerate 得到正在运行的子线程，即子线程1和子线程3
    for thr in threading.enumerate():
        #getName得到线程的名字
        print("正在运行的线程名字是：{0}".format(thr.getName()))

    print("正在运行的线程数量是：{0}".format(threading.activeCount()))

    print("All done at:",time.ctime())

if __name__ == '__main__':
    main()
    #其实是有三个线程在运行，一个主线程，用于分配工作；另外两个是工作的线程
    #然后这个是等待所有工作线程工作完
    #这个循环不会停止线程的运行，所以使用时注意关闭，否则不会往下执行
    # while True:
    #     time.sleep(1)
print("======================================")
#由于上面导入过threading和time了，就不再重复导入了

#1、类需要继承自threading.Thread
#把需要执行的都写在run函数内
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread,self).__init__()
        self.arg = arg
    #2、必须重写run函数，run函数代表的是真正执行的功能，这个也是不需要再次调用
    def run(self):
        time.sleep(2)
        print("The args for this class is {0}".format(self.arg))

for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()

print("Main thread is done!!!!")








