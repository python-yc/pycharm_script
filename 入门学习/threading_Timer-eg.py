"""
import threading
import time

def func():
    print("I am running........")
    time.sleep(4)
    print("I am done.........")

if __name__ == '__main__':
    t = threading.Timer(6,func)
    t.start()

    i = 0
    while True:
        print("{0}********".format(i))
        time.sleep(3)
        i += 1
        if i >= 10:
            break
"""
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if  mutex.acquire(1):
            num = num + 1
            msg = self.name+'set num to '+str(num)
            print(msg)
            mutex.acquire()
            mutex.release()

num = 0

mutex = threading.RLock()

def testTh():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    testTh()









