Format Description
%(name)s        Name of the logger (logging channel).
%(levelno)s     Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL).
%(levelname)s   Text logging level for the message ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL').
%(pathname)s    Full pathname of the source file where the logging call was issued (if available).
%(filename)s    Filename portion of pathname.
%(module)s      Module (name portion of filename).
%(funcName)s    Name of function containing the logging call.
%(lineno)d      Source line number where the logging call was issued (if available).
%(created)f     Time when the LogRecord was created (as returned by time.time()).
%(relativeCreated)d     Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.
%(asctime)s             Human-readable time when the LogRecord was created. By default this is of the form “2003-07-08 16:49:45,896” (the numbers after the comma are millisecond portion of the time).
%(msecs)d               Millisecond portion of the time when the LogRecord was created.
%(thread)d      Thread ID (if available).
%(threadName)s      Thread name (if available).
%(process)d         Process ID (if available).
%(message)s     The logged message, computed as msg % args.
---------------------
作者：socrates
来源：CSDN
原文：https://blog.csdn.net/dyx1024/article/details/7250828
版权声明：本文为博主原创文章，转载请附上博文链接！


字段/属性名称	使用格式	描述
asctime	%(asctime)s	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
created	%(created)f	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
relativeCreated	%(relativeCreated)d	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
msecs	%(msecs)d	日志事件发生事件的毫秒部分
levelname	%(levelname)s	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
levelno	%(levelno)s	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
name	%(name)s	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
message	%(message)s	日志记录的文本内容，通过 msg % args计算得到的
pathname	%(pathname)s	调用日志记录函数的源码文件的全路径
filename	%(filename)s	pathname的文件名部分，包含文件后缀
module	%(module)s	filename的名称部分，不包含后缀
lineno	%(lineno)d	调用日志记录函数的源代码所在的行号
funcName	%(funcName)s	调用日志记录函数的函数名
process	%(process)d	进程ID
processName	%(processName)s	进程名称，Python 3.1新增
thread	%(thread)d	线程ID
threadName	%(thread)s	线程名称
