import time
import threading

def fun():
    print("Start fun")
    time.sleep(3)
    print("End fun")

def main():
    print("Starting at:",time.ctime())
    t1 = threading.Thread(target=fun,args=())
    t1.start()
    time.sleep(1)
    print("Main thread end")

if __name__ == '__main__':
    main()







