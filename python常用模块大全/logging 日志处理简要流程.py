# -*- coding: utf-8 -*-
import logging

"""
此例子日志同时写进两个文件，级别不同

四、日志处理的简要流程
4.1、创建一个logger，由logger产生日志
4.2、设置logger日志的等级
4.3、创建合适的Handler（FileHandler要有路径）
4.4、设置每个Handler的日志等级
4.5、创建日志的格式（# setFormatter 输出到控制台设置日志等是不生效的）
4.6、向Handler中添加上面创建的Handler格式
4.7、将上面的Handler添加到logger中
4.8、打印日志
"""

# 4.1、创建一个logger
logger = logging.getLogger('logger_1')

# 4.2、设置logger日志的等级
logger.setLevel(logging.DEBUG)

# 4.3、创建合适的Handler
# 文件句柄  重定向到多个文件中，添加多个file_handler 即可，配置自定义
file_handler = logging.FileHandler('test.log', encoding='utf-8')
file_handler2 = logging.FileHandler('all.log', encoding='utf-8')
# 控制台句柄
consle_handler = logging.StreamHandler()

# 4.4、设置每个Handler的日志等级
file_handler.setLevel(logging.INFO)
file_handler2.setLevel(logging.DEBUG)
# setFormatter 设置日志等是不生效的
consle_handler.setFormatter(logging.ERROR)

# 4.5、创建日志的格式
# 注意logger.Formatter的大小写
# [%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d][%(levelname)s][%(messages)s]
formatter = logging.Formatter(
    # fmt = "%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s",
    fmt="[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s]"
        "[%(filename)s:%(lineno)d][%(levelname)s][%(message)s]",
    datefmt="%Y-%m-%d %X"
)

# 4.6、向Handler中添加上面创建的Handler格式
file_handler.setFormatter(fmt=formatter)
file_handler2.setFormatter(fmt=formatter)
consle_handler.setFormatter(fmt=formatter)

# 4.7、将上面的Handler添加到logger中
logger.addHandler(file_handler)
logger.addHandler(file_handler2)
logger.addHandler(consle_handler)

# 4.8、打印日志
logger.debug("-----debug-----")
logger.info("-----info-----")
logger.warning("-----warning-----")
logger.error("-----error-----")


"""
logging终极解决方案
一、logging的继承（了解）

可以将一个日志指定为另一个日志的子日志或者孙日志，当存在继承关系时，子孙级日志收到日志时
会将该日志向上传递指定继承关系：
"""
log1 = logging.getLogger("father")
log2 = logging.getLogger("father.son")
log3 = logging.getLogger("father.son.grandson")

# fh = logging.FileHandler(filename="cc.log", encoding="utf-8")
ch = logging.StreamHandler()
fm = logging.Formatter("%(asctime)s - %(name)s -%(filename)s - %(message)s")

log1.addHandler(ch)
log2.addHandler(ch)
log3.addHandler(ch)

ch.setFormatter(fm)

# 测试
# log1.error("test")
# log2.error("test")
log3.error("test")

log1.error("----------split: 3 before, 1 after------------")

# 取消传递
log3.propagate = False
# # 再次测试
log3.error("test")
