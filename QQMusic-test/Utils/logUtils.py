import logging
import os.path
import time

class InfoFilter:
    def filter(self, record):
        return record.levelno == logging.INFO

class ErrorFilter:
    def filter(self, record):
        return record.levelno == logging.ERROR


class Logger:
    logger = None
    @classmethod
    def getLog(cls):

        # 创建日志对象
        if cls.logger is None :
            cls.logger = logging.getLogger(__name__)
        # 设置日志级别
        cls.logger.setLevel(logging.DEBUG)

        LOG_PATH = "log/"
        if not os.path.exists(LOG_PATH):
            os.mkdir(LOG_PATH)

        now = time.strftime("%Y,%m,%d")

        logname = LOG_PATH + now + ".log"
        info_logname = LOG_PATH + now + "_info.log"
        error_logname = LOG_PATH + now + "_error.log"

        # 创建日志文件处理器
        handler = logging.FileHandler(logname, encoding="UTF-8")

        info_handler = logging.FileHandler(info_logname, encoding="UTF-8")
        info_handler.addFilter(InfoFilter())

        error_handler = logging.FileHandler(error_logname, encoding="UTF-8")
        error_handler.addFilter(ErrorFilter())

        # 设置日志格式
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
        )

        handler.setFormatter(formatter)

        info_handler.setFormatter(formatter)

        error_handler.setFormatter(formatter)

        cls.logger.addHandler(handler)
        cls.logger.addHandler(info_handler)
        cls.logger.addHandler(error_handler)

        return cls.logger