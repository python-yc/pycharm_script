import multiprocessing
from time import sleep,ctime

def clock(interval):
    num = 1
    while True:
        #print("The time is %s" %ctime())
        print("The time is {0}".format(ctime()))
        sleep(interval)
        num += 1
        if num >=5:
            break

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock,args=(3,))
    p.start()











