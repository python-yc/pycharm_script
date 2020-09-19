# 1 open 函数
- 负责打开文件，有较多参数选择
- 第一个参数：必须有，文件的路径和名称
- mode：表明文件有什么方式打开
    r ：以只读方式打开
    w ：写方式打开，会覆盖已有文件，如果文件不存在会创建文件
    a ：append以追加方式打开，如果文件不存在创建文件
    x ：创建方式打开，如果文件存在，报错
    b ：binary，以二进制方式写入
    t ：文本方式打开
    + ：可读写
- 案例open-eg
## tell 函数
- 案例open-eg
## 文件的写操作write
- write(str):把字符串写入文件
- writelines(str):把字符串按行写入文件
- 区别：
    write函数参数只能是字符串
    writelines参数可以是字符串，也可以是字符串序列
    - 案例open-eg
##序列化 - pickle
- 也成为持久化，落地：把程序 运行中 的信息保存在磁盘上
##反序列化：序列化的逆过程（把磁盘上读出来，但不仅只是读）
- pickle：python提供的序列化模块
- pickle.dump：序列化
- pickle.load：反序列化
    - 案例open-eg
##序列化-shelve
- 持久化工具
- 类似字典，用k,v保存数据，存取方式跟字典也类似
- open，close
#- shelve 特殊性
- 不支持多个应用并行写入
# 2 LOG
- 案例LOG-eg
- https://www.cnblogs.com/yyds/p/6901864.html
- logging 模块
- logging模块提供模块界别的函数记录日志 --包括四大组件
## 2.1 日志相关概念
- 日志级别（level）
    - 不同用户关注不同级别程序信息
    - DEBUG、INFO、NTOICE、WARING、ERROR、CRITICAL、ALERT、EMERGENCY
- IO操作=>不要太频繁
- LOG的作用
    - 调试、了解软件的运行情况、分析定位问题
- 日志信息
    - time、路径（地点）、行号、level、内容
- 成熟的第三方
    - log4j、log4php、logging
##2.2 logging模块
- 日志级别
    - DEBUG、INFO、WARING、ERROR、CRITICAL
- 初始化/写日志实例需要制定级别，只有级别大于等于制定级别时才会被记录
- 使用方式
    - 直接使用logging(封装了其他组件)
    - logging四大组件直接定制
##2.2.1 logging模块级别的日志
- 一般使用以下几个函数，足以使用：
    logging.debug(msg,*args,**kwargs)   创建一条严重级别为DEBUG的日志记录
    logging.info(msg,*args,**kwargs)   创建一条严重级别为INFO的日志记录
    logging.warning(msg,*args,**kwargs)   创建一条严重级别为WARNING的日志记录
    logging.error(msg,*args,**kwargs)   创建一条严重级别为ERROR的日志记录
    logging.critical(msg,*args,**kwargs)   创建一条严重级别为CRITICAL的日志记录
    logging.log(level,*args,**kwargs)   创建一条严重级别为level的日志记录
    logging.basicConfig(**kwargs)   对root logger进行一次性配置
    
- logging.basicConfig(**kwargs)   对root logger进行一次性配置
    - 只在第一次使用的时候起作用
    - 不配置logger则使用## 默认 ##值
        -输出：sys.stderr
        -级别：WARNING(若想修改，使用basicConfig()进行修改)
        -格式：level：log_name:content
        -其中format参数有很多默认值
        -案例LOG-eg
##2.2.2 logging 模块的处理流程
- 四大组件
    - 日志器(Logger)：产生日志的第一个接口
    - 处理器(Handler)：把产生的日志发送到相应的目的地
    - 过滤器(Filter)：更精细地控制哪些日志输出
    - 格式器(Formatter)：对输出信息进行格式化
-#Logger
    - 产生一个日志
    - 操作
        Logger.setLevel()   设置日志处理器将会处理的日志消息的最低严重级别
        Logger.addHandler() 和Logger.removeHandler()   为该logger对象添加或者移除一个处理器
        Logger.addFilter() 和Logger.removeFilter()   为该logger对象添加或者移除一个过滤器
        Logger.debug:产生一条debug级别的日志，同理 info、error等
        Logger.exception():创建一个类似于Logger.error的日志消息
        Logger.log():获取一个明确的日志level参数类创建一个日志记录
    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()
-#Handler类
    - 把log发送到指定位置
    - 方法
        - setLevel、setFormat、addFilter,removeFilter
    #####- 不需要直接使用，Handler是基类(基类是给其它类继承用的)
        logging.StreamHandler       将日志消息发送到输出到Stream，如std.err或任意file-like对象
        logging.FileHandler         将日志消息发送到磁盘文件，默认情况下文件大小无限增长
        logging.handlers.RotatingFileHandler    将日志消息发送到磁盘文件，并支持日志文件按文件大小切割
        logging.handlers.TimedRotatingFileHandler   将日志消息发送到磁盘文件，并支持日志文件按时间切割
        logging.handlers.HTTPHandler    将日志消息以GET或PSOT的方式发给一个HTTP服务器
        logging.handlers.SMTPHandler    将日志消息发送给一个指定的email地址
        logging.NullHandler 该Handler实例会忽略error messages，通常被想使用logging的library开放
-#Format类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数：
        - fmt:指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        - datefmt:指定日期格式字符串，如果不指定默认为"%Y-%m-%d %H:%M:%S"
        - style:python 3.2新增参数，可取值为'%','{',和'$'，如果不指定该参数，默认使用'%'
-#Filter类
    - 可以被Handler和Logger使用
    - 控制传递过来的信息的具体内容
- 案例 LOG-eg
# 3 多线程
-#3.1 环境
    - xubuntu 16.04、anaconda、pycharm、python3.6
    - https://www.cnblogs.com/jokerbj/p/7468268.html
    - http://www.dabeaz.com/python/UnderstandingGIL.pdf
-#多线程 vs 多进程
- 程序：一堆代码以文本形式存入文档
- 进程：程序运行的一个状态
    - 包含地址空间、内存、数据栈等
    - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
        - 一个进程的多个线程间共享数据和上下文运行环境
        - 共享互斥问题
- 全局解释器锁（GIL）
    - python代码的执行是由python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行
- python包
    - thread 有问题，不好用，python3改成了_thread（不推荐）
    - threading     通行的包
    - 案例thread-eg
    - 多线程传参数
    - 案例thread-eg-01
    - threading的使用
        - 直接利用threading.Thread生成Thread实例
        （调用Thread时，会自动执行run函数，所以必要时需要重写run函数）
            1、t = threading.Thread(target=xxx,args=(xxx,))
            2、t.start():启动多线程
            #这个是为了不总是用while进行等待，而换成了join
            3、t.join():等待多线程完成
            - 案例threading-eg
            - jion()：案例threading-eg-01与threading-eg比较
            #守护线程-daemon
                - 如果在程序中将子线程设置为守护线程，则子线程会在主线程结束时自动退出
                - 一般认为，守护线程不重要或者不允许离开主线程独立运行
                - 守护线程案例能否有效果与环境相关
                - 守护线程案例guard-eg与非守护线程案例guard_un-eg
            #线程常用属性
                - threading.currentThread():返回当前线程变量
                - threading.enumerate():返回一个包含正在运行的线程的list，正在运行的线程指的是启动后，结束前
                - threading.activeCount():返回正在运行的线程数量，效果与len(threading.enumerate)相同
                - thr.setName(name):给线程设置名称
                - thr.getName(name):得到线程的名称（thr为实例名称）
                - 案例threading_property_eg
            #直接继承自threading.Thread
                - 直接继承Thread，有两个函数注意
                    - 1、init函数；2、run函数
                - 重写run函数
                - 类实例可以直接运行，把所需执行部分写在run函数内
                - 案例threading_property_eg
# 3.2 共享变量
    - 当多个线程同时访问一个变量的时候，会产生共享变量的问题
    - 案例public_threading-eg
    - 解决变量：锁，也叫信号灯
    - 锁：(Lock)
        - 是一个标志，表示一个线程在占用一些资源，其它不能再使用
        - 使用方法：
            - 上锁
            - 放心的使用共享资源
            - 取消锁，释放锁
            - 案例public_threading-eg
#-线程安全问题
    - 如果一个资源/变量，他对于多线程来讲，不用加锁也不会引起任何问题，则成为线程安全(如果只读也可以)
    - 线程不安全类型：list、set、dict
    - 安全的有queue
#-生产者消费者问题
    - 一个模型：可以用来搭建消息队列
    - queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队
    - 案例queue-eg
#-死锁问题
    - 案例threading_dead_lock-eg
#   - 解决锁的等待时间，即解决死锁问题
    - semphore
        - 允许一个资源最多由几个多线程同时使用
        - 案例semaphore-eg
#-threding_Timer
    - 案例threading_Timer-eg
    - 利用多线程在指定时间后产生一个功能
#-可重入锁
    - 一个锁，可以被一个线程多次申请
    - 主要解决递归调用的时候，需要申请锁的情况
    - 案例threading_Timer-eg
##-进程代替线程
- subprocess
    - 完全跳过线程，使用进程
    - 是派生进程的主要代替方案
    - python2.4引入
- multiprocessing
    - 使用threading接口派生，使用子进程
    - 允许为多核或者多cpu派生进程，接口与threading非常相似
    - python2.6引入
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - python3.2引入
##-多进程
- 进程间通讯(InterProcessCommunication,IPC)
- 进程之间无任何共享
- 进程的创建
    - 直接生成Process实例对象，案例process-eg
    - 派生子类
- 在os中查看pid，ppid以及他们的关系
- 案例process_pid_ppid-eg
- 生产者消费者模型
    - JoinableQueue     支持通知作用
    - 案例JoinableQueue-eg
    - 队列中哨兵的使用
    - 案例process_sentinel-eg
# 4 协程
- 参考资料：
    - http://python.jobbole.com/86481
    - http://python.jobbole.com/87310
    - https://segmentfault.com/a/1190000009781688
# 4.1 迭代器
- 可迭代(Iterable)：直接作用于for循环的变量
- 迭代器(Iterator)：不但可以作用于for循环，还可以被 ##next##调用
- list是典型的可迭代对象，但不是迭代器,不能被next调用
- range()就是一个迭代器
# 4.2 迭代器的判断
- 通过isinstance判断
- Iterable与Iterator可以转换
    通过iter函数进行转换
- 案例Iterable-eg
# 4.3 生成器
- generator：是一个一边循环一边计算下一个元素的机制/算法
- 需要满足三个条件：
    - 每次调用都生产出for循环需要的下一个元素
    - 如果达到最后一个后，爆出StopInteration异常
    - 可以被next函数调用
    - 案例Iterable-eg
- 如何生成一个生成器
    - 直接使用
    - 如果函数中包含yield，则这个函数就叫生成器
    - next调用函数，遇到yield返回
    - 案例Iterable-eg
# 4.4 协程
- 历史历程
    - 3.4引入协程，用yield实现
    - 3.5引入协程语法
    - 实现的协程比较好的包有asyncio、tornado、gevent
- 定义：协程是为了非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停
或开始执行程序；
- 从技术角度讲，协程就是一个你可以暂停执行的函数，或者干脆把协程理解成生成器
- 协程的实现：
    - yield返回或者send调用
    - 案例coroutine-eg
- 协程的四个状态：
    - inspect.getgeneratorstate(...) 函数确定，该函数会返回下述字符串中的一个
        - GEN_CREATED:等待开始执行
        - GEN_RUNNING:解释器正在执行
        - GEN_SUSPENED:在yield表达处暂停
        - GEN_CLOSED:执行结束
    - next预激(prime)
    - 案例coroutine-eg
- 协程终止
    - 协程终止未处理的异常会向上冒泡，传给next函数或send方法的调用方，
即触发协程的对象。
    - 终止协程的一种方式：发送某个哨符值，让协程退出。内置的None和Ellipsis
等常量经常用作哨符值。
- yield from
    - 调用协程为了得到返回值，协程必须正常终止
    - 生成器正常终止会发出StopIteration异常，异常对象的value属性保存返回值
    - yield from从内部捕获StopIteration异常
    - 案例coroutine-eg
    - 委派生成器
        - 包含yield from表达式的生成器函数
        - 委派生成器在yield from表达式处暂停，调用方可以直接把数据发给子生成器
        - 子生成器在把产出的值发给调用方
        - 子生成器在最后，解释器会抛出StopIteration异常，并且把返回值附加到异常对象上
# 4.4.1 asyncio
- python3.4开始引入标准库当中，内置对异步io的支持
- asyncio本身是一个消息循环
- 步骤：  
    - 创建消息循环
    - 把协程导入
    - 关闭
    - 案例asyncio-eg
# 4.4.2 async and await
- 为了更好的表示异步io
- python3.5引入，让协程代码更简洁
- 使用上可以简单的进行替换
    - 用async替换@asyncio.coroutine
    - await替换yield from
    - 案例asyncio-eg
# 4.4.3 aiohttp
- asyncio实现单线程并发的io，在客户端用户不大
- 在服务器端可以asyncio+coroutine配合，因为http是io操作
- asyncio实现了tcp、udp、ssl等协议
- aiohttp是给予asyncio实现的http框架
- pip install aiohttp安装
- 案例代码aiohttp-eg(pycharm无aiohttp环境，pip安装后在jupyter上运行)
# 4.4.4 concurrent.futures
- python3新增的库
- 类似其它语言的线程池的概念
- 利用multiprocessing实现真正的并行计算
- 核心原理：以子进程的形式，并行运行多个python解释器，从而令python程序可以
利用多核CPU来提升执行速度。由于子进程与主解释器相分离，所以他们的全局解释器锁也是
相互独立的。每个子进程都能够完整的使用一个CPU内核。
- - concurrent.futures.Executor
    - ThreadPoolExecutor
    - ProcessPoolExecutor
    - 执行的时候需要自行选择
- submit(fn,args,kwargs)
    - fn:异步执行函数
    - args，kwargs参数
    -案例concurrent.futures-eg
# current中的map函数
- map(fn,\*iterables,timeout=None)
    - 跟map函数类似
    - 函数需要异步执行
    - timeout：超时时间
    - map 与submit使用一个就可以
     -案例concurrent.futures-eg
 # Future   未来实现的事情，但是会发生；即先用一个空的来代表着，当过了一段时间再替换过去


