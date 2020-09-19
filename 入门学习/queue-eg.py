#encoding:utf-8
import threading
import time

#python2
#from Queue import Queue

#python3
import queue

class Producter(threading.Thread):
    #调用Thread时会自动执行的函数，所以要重写run函数，即真正干活的人是run
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = '生成产品'+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    #get是从queue中取出一个值
                    msg = self.name + '消费了'+queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品'+str(i))
    #生成了两个生产者
    for i in range(2):
        p = Producter()
        p.start()
    #生成了五个消费者
    for i in range(5):
        c = Consumer()
        c.start()




