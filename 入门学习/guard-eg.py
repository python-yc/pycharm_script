import time
import threading

def fun():
    print("Start fun")
    time.sleep(5)
    print("End fun")

def main():
    print("Starting at:",time.ctime())
    t1 = threading.Thread(target=fun,args=())
    #守护线程的方法，必须在start之前设置，否则无效
    t1.setDaemon(True)
    # 或者这样写
    # t1.Daemon = True

    t1.start()
    print(threading.currentThread())
    print(threading.enumerate())
    print(threading.activeCount())
    time.sleep(3)
    print("Main thread end")

if __name__ == '__main__':
    main()

















