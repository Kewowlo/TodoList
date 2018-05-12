# coding=utf-8
import logging
import tornado.log
from config import LOG_CONFIG

def init(port, console_handler=False, file_handler=True, log_path=None, base_level="INFO"):
    logger = logging.getLogger()
    logger.setLevel(base_level)
    #控制台输出
    if console_handler:
        channel_console = logging.StreamHandler()
        channel_console.setFormatter(tornado.log.LogFormatter())
        logger.addHandler(channel_console)
    
    #文件输出
    if file_handler:
        if not log_path:
            log_path = LOG_CONFIG['log_path']
        log_path = log_path+"@"+str(port)+".txt"
        formatter = logging.Formatter(LOG_CONFIG['fmt'])
        channel_file = logging.handlers.TimedRotatingFileHandler(
            filename=log_path,
            when=LOG_CONFIG['when'],
            interval=LOG_CONFIG['interval'],
            backupCount=LOG_CONFIG['backupCount'])
        channel_file.setFormatter(formatter)
        logger.addHandler(channel_file)
