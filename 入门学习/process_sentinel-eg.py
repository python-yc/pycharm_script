'''
import multiprocessing
from time import ctime

def consumer(input_q):
    print('into consumer:',ctime())
    while True:
        #处理项
        item = input_q.get()
        if item is None:
            break
        #此处替换为有用的工作
        print("pull",item,"out of q")
    #此句执行完成，再转入主进程
    print("Out of consumer:",ctime())

def producer(sequence,output_q):
    print("Into producer:",ctime())
    for item in sequence:
        output_q.put(item)
        print("put",item,"into q")
    print("Out of producer:",ctime())

#建立进程
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    cons_p.start()
    #生产多个项，sequence代表要发送给消费者的项序列
    #在实践中，这可能是生成器的输出或通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence,q)
    q.put(None)
    cons_p.join()
'''
#哨兵作用的该进，上面的由于一个消费者将None取出后，后面的消费者将取不到None，则不能下班
#但是有几个哨兵值，需要放几个None或者其它自设置的值
import multiprocessing
from time import ctime

def consumer(input_q):
    print('into consumer:',ctime())
    while True:
        #处理项
        item = input_q.get()
        if item is None:
            break
        #此处替换为有用的工作
        print("pull",item,"out of q")
    #此句执行完成，再转入主进程
    print("Out of consumer:",ctime())

def producer(sequence,output_q):
    print("Into producer:",ctime())
    for item in sequence:
        output_q.put(item)
        print("put",item,"into q")
    print("Out of producer:",ctime())

#建立进程
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    cons_p1 = multiprocessing.Process(target=producer,args=(q,))
    cons_p1.start()

    cons_p2 = multiprocessing.Process(target=consumer,args=(q,))
    cons_p2.start()

    sequence = [1,2,3,4]
    producer(sequence,q)

    q.put(None)
    q.put(None)

    cons_p1.join()
    cons_p2.join()





