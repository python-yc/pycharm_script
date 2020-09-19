'''
import threading
#引入异步io包
import asyncio

#使用协程
@asyncio.coroutine
def hello():
    print('Hello world! (%s)'% threading.currentThread())
    print('Start...(%s)'%threading.currentThread())
    yield from asyncio.sleep(5)
    print('Done.....(%s)' %threading.currentThread())
    print('Hello again!.....(%s)' %threading.currentThread())

#启动消息循环
loop = asyncio.get_event_loop()
#定时任务
tasks = [hello(),hello()]
#asyncio使用wait等待task执行完毕
loop.run_until_complete(asyncio.wait(tasks))
#关系消息循环
loop.close()
结果：
Hello world! (<_MainThread(MainThread, started 10648)>)
Start...(<_MainThread(MainThread, started 10648)>)
Hello world! (<_MainThread(MainThread, started 10648)>)
Start...(<_MainThread(MainThread, started 10648)>)
Done.....(<_MainThread(MainThread, started 10648)>)
Hello again!.....(<_MainThread(MainThread, started 10648)>)
Done.....(<_MainThread(MainThread, started 10648)>)
Hello again!.....(<_MainThread(MainThread, started 10648)>)
'''

# asyncio案例2
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' %host)
    #异步请求网络地址
    connect = asyncio.open_connection(host,80)
    #注意yield from的用法
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s/r/n/r/n' %host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        #http协议的换行使用\r\n
        if line == b'\r\n':
            break
        print('%s header > %s' %(host,line.decode('utf-8').rstrip()))
    #Ignore the body,close the socket
    writer.close()
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

"""
# 案例3  async、await的使用，具体怎么简单了，其实并不能体现出来
import threading
#引入异步io包
import asyncio

#使用协程
##@asyncio.coroutine###############
async def hello():
    print('Hello world! (%s)'% threading.currentThread())
    print('Start...(%s)'%threading.currentThread())
    ########yield from asyncio.sleep(5)#########
    await.asyncio.sleep(5)
    print('Done.....(%s)' %threading.currentThread())
    print('Hello again!.....(%s)' %threading.currentThread())

#启动消息循环
loop = asyncio.get_event_loop()
#定时任务
tasks = [hello(),hello()]
#asyncio使用wait等待task执行完毕
loop.run_until_complete(asyncio.wait(tasks))
#关系消息循环
loop.close()
"""







