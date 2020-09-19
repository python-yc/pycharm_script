#LOG
# https://www.cnblogs.com/yyds/p/6901864.html
import logging

'''
- logging.basicConfig(**kwargs)   对root logger进行一次性配置
    - 只在第一次使用的时候起作用
    - 不配置logger则使用## 默认 ##值
        -输出：sys.stderr
        -级别：WORRING(若想修改，使用basicConfig()进行修改)
        -格式：level：log_name:content
'''
#自动义样式
LOG_FORMAT = "%(asctime)s=====%(levelname)s++++%(message)s"


#使用basicConfig()进行修改日志级别，以便于得到所需信息
logging.basicConfig(filename="C:/running.log",level=logging.DEBUG,format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

print("===============中间这个线条不会对上下日志输出位置有分割====================")
#另外一种写法
logging.log(logging.DEBUG,"This is a debug log.")
logging.log(logging.INFO,"This is a info log.")
logging.log(logging.WARNING,"This is a warning log.")
logging.log(logging.ERROR,"This is a error log.")
logging.log(logging.CRITICAL,"This is a critical log.")

"""
现在有以下几个日志记录的需求：
    1） 要求将所有级别的日志都写入磁盘文件中
    2） all.log文件中记录所有的日志信息，日志格式：日期和时间-日志级别-日志信息
    3） error.log文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间-日志级别-文件名[:行号]-日志信息
    4） 要求all.log在每天凌晨进行日志切割
"""
import logging
import logging.handlers
import datetime

#定义logger
logger = logging.getLogger('mylogger.log')      #mylogger.log这像一个参数，被传入方法呢，我知道的并未使用（自己未找到）
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('C:\\all.log',when='Midnight',interval=1,backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

f_handler = logging.FileHandler('C:\\error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d]-%(message)s"))

#把相应的处理器组装到logger上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

