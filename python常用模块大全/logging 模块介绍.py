# -*- coding: utf-8 -*-
import logging

# https://www.cnblogs.com/wf-linux/archive/2018/08/01/9400354.html
# https://blog.csdn.net/weixin_43298313/article/details/106934176?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.channel_param

# 基本使用，配置logging基本的设置，然后在控制台输出日志
level = logging.INFO
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.basicConfig(level=level, format=format)
logger = logging.getLogger(__name__)

logger.info('info...')
logger.debug('debug...')
logger.warning('warning...')
logger.info('use logger finish...')
logging.info('use logging finish...')

"""
logging.basicConfig函数各参数：
filename：指定日志文件名；
filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
format：指定输出的格式和内容，format可以输出很多有用的信息，

参数：作用
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息

datefmt：指定时间格式，同time.strftime()；
level：------设置日志级别，默认为logging.WARNNING；------
stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；


一、logging模块的四个核心角色
Logger — 提供了应用程序一直可以使用的接口
Filter — 日志过滤器，过滤日志（提供了更细粒度的控制工具来决定输出哪条日志，丢弃哪条日志）
Handler — 日志处理器，用于对日志进行格式化，输出到指定的位置（控制台或者文件）
Formatter — 处理日志的格式（决定日志记录的最终输出格式）

二、这些组件之间的关系描述：
Logger（日志器）需要通过Handler（处理器）将日志信息输出到目标位置，如控制台或者文件中等。
不同的Handler（处理器）可以将日志输出到不同的位置。
Logger（日志器）可以设置多个处理器将同一条日志记录输出到不同的位置。
每个Handler（处理器）都可以设置自己的Filter（过滤器）来实现日志过滤，从而只保留感兴趣的日志。
每个Handler（处理器）都可以设置自己的Formatter（格式器）实现同一条日志以不同的格式输出到不同的地方。
总结来说就是Logger是入口，真正干活的是Handler，Handler还可以通过Filter和Formatter对要输出的日志内容做过滤和格式化等处理操作。

三、logging日志模块相关类以及常用方法介绍
1、Logger
Logger对象有三个任务要做：
1）向应用程序代码提供几个方法，使得应用程序可以在运行时记录日志的消息。
2）基于日志严重等级（默认的过滤设施）或者Filter对象（更细粒度的过滤）来决定要对哪些日志进行后续处理。
3）将日志消息产送给感兴趣的日志Handler。
Logger对象最常用的方法分为两类：配置方法和消息发送方法。

1）配置方法
Logger.setLevel() — 设置日志器将会处理的消息的最低级别
Logger.addHandler() & Logger.removeHandler() — 为该logger对象添加和移除一个Handler对象
Logger.addFilter() & Logger.removeFilter() — 为该logger对象添加和移除一个Filter对象
logger对象配置完成后，可以通过以下方法来创建日志记录

2）日志记录创建方法
Logger.debug() & Logger.info() & Logger.warning() & Logger.error() $ Logger.critical() — 创建一个对应等级的日志记录
Logger.exception() — 创建一个类似于Logger.error()的日志消息
Logger.log() — 需要获取一个明确的日志level参数来创建一个日志记录


一个logger对象怎么创建？
一种方法是使用将Logger类实例化的方法来创建，但是通常使用第二种方法：logging.getLogger().
logging.getLogger()方法有一个可选参数name，该参数表示要返回的Logger（日志器）的名称标识，如果不提供该参数，那么默认值为"root"，若以相同的方法多次调用getLogger()方法，将会返回同一个logger对象的引用。

2、Handler
Handler类的作用是（基于日志消息的level）将消息分发到handler指定的位置（文件、控制台等）。Logger对象可以通过addHandler()方法为自己添加1个或者更多个handler对象，比如，一个应用程序可能想要实现以下几个日志需求：
把所有日志都发送到一个日志文件中
把所有严重级别大于等于error的日志控制台输出
把所有严重级别为critical的日志单独写入一个日志文件中

实现以上三个需求就需要三个handler。
需要说明的是，应用程序代码不应该直接实例化和使用Handler实例，因为Handler是一个基类，它只定义了所有Handler子类都应该有的接口，同时提供了一些子类可以直接使用或者覆盖的默认行为，下面是一些常用的Handler：
logging.StreamHandler — 将日志消息发送到输出Stream，例如控制台输出或者任何file-like对象
logging.FileHandler — 将日志消息发送到磁盘文件，默认情况下，文件大小会无限增长
logging.handlers.RotatingHandler — 将日志消息发送到磁盘文件，并支持日志文件按照大小切割
logging.handlers.TimedRotatingFileHandler — 将日志消息发送到磁盘文件，并支持日志文件按照时间切割
logging.handlers.HTTPHandler — 将日志消息以GET或者POST的方式发送给一个HTTP服务器
logging.handlers.SMTPHandler — 将日志消息发送给一个指定的Email地址
logging.NullHandler — 该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免“No handlers could be found for logger XXX"信息的出现

3、Filter（暂时了解）
Filter可以被Handler进而Logger用来做比level更细粒度的、更复杂的过滤功能。Filter是一个过滤器基类，它只允许某个logger层级下的日志时间通过过滤，该类定义如下：
class logging.Filter(name="")
    filter(record)

比如，一个filter实例化时传递的name参数值为"A, B"，那么该filter实例将只允许名称为类似如下规则的loggers产生的日志通过过滤：“A.B”,“A.B.C”,“A.B.C.D”,“A.B.D”，而名称为"A.BB","B.A.B"的loggers产生的日志则会被过滤，如果name的值为空字符串，那么允许所有的日志事件通过过滤。
filter方法用于具体控制传递的record记录是否能通过过滤，如果该方法返回值为0表示不能通过过滤，返回值非0表示可以通过过滤。

4、Formatter
Formater会先用于配置日志信息的最终顺序、结构和内容。与logging.Handler基类不同的是，应用程序代码可以直接实例化Formatter类，另外，如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成。
Formatter类的构造方法如下：
logging.Formatter.__init__(fmt=None,datefmt=None,style="%")

可见，该构造方法接收三个可选参数：
fmt：指定消息格式化字符串，如果不指定则使用message的原始值
datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
style：Python3.2新增加的参数，可取值为”%“，和"{"，"$"，如不指定该蚕食则默认使用"%"
一般直接用logging.Formatter(fmt, datefmt)


四、日志处理的简要流程
4.1、创建一个logger，由logger产生日志
4.2、设置logger日志的等级
4.3、创建合适的Handler（FileHandler要有路径）
4.4、设置每个Handler的日志等级
4.5、创建日志的格式
4.6、向Handler中添加上面创建的Handler格式
4.7、将上面的Handler添加到logger中
4.8、打印日志
"""
