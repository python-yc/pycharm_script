# -*- coding: utf-8 -*-
import logging.config

standard_format = "[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]" \
                  "[%(levelname)s][%(message)s]"  # 其中name为getLogger指定的名字
simple_format = "[%(levelname)s][%(asctime)s] %(message)s"
logfile_path = "ab.txt"

LOGGING_DIC = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": standard_format,
        },
        "simple": {
            "format": simple_format
        }
    },
    "filters": {},
    "handlers": {
        # 打印到终端的日志
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        # 打印到文件的日志，收集info及以上的日志
        "default": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standrd",
            "filename": logfile_path,
            "maxBytes": 1024 * 1024 * 5,
            "backupCount": 5,
            "encoding": "utf-8"
        }
    },
    "loggers": {
        # logging.getLogger(__name__)拿到的logger配置
        "aa": {
            "handlers": ["default", "console"],
            "level": "DEBUG",
            "propagate": True
        }
    }
}

logging.config.dictConfig(LOGGING_DIC)
logging.getLogger('aa').debug("debugb message")
