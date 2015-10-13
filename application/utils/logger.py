# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/09 14:57


import logging

from application.utils.mq_log import MQHandler
from application.configure import setting


#The background is set with 40 plus the number of the color, and the foreground with 30
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = [30 + i for i in range(8)]

#These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


def format_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message

COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED
}


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color = True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        level = record.levelname

        if self.use_color and level in COLORS:
            level_color = COLOR_SEQ % COLORS[level] + level + RESET_SEQ
            record.levelname = level_color

        return logging.Formatter.format(self, record)


def get_logger(name=__name__, log_level='debug', log_file=None):
    _log_level = getattr(logging, log_level.upper(), None)

    if not _log_level:
        raise Exception("No such log level. log level should be one of notest, debug, info, warning, error, critical.")

    logger = logging.getLogger(name)
    logger.setLevel(_log_level)

    if log_file is not None:
        handler = logging.FileHandler(log_file)
    else:
        handler = MQHandler(setting.AMQP_HOST, setting.AMQP_PORT, setting.AMQP_USER_NAME, setting.AMQP_PASSWORD,
                            setting.AMQP_EXCHANGE, virtual_host=setting.AMQP_VIRTUAL_HOST,
                            machine_id=setting.MACHINE, process_id=setting.PROCESS)

    formatter = ColoredFormatter("%(asctime)s\t%(process)d|%(thread)d\t%(levelname)s\t%(module)s\t%(funcName)s:%(lineno)d\t%(message)s", "%Y-%m-%d@%H:%M:%S")
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

flask_logger = get_logger("flask_log", 'debug', setting.LOG_PATH)
# flask_logger = get_logger("flask_log", 'debug')
#
# import time
#
# start = time.time()
# flask_logger.error("Hello World")
# print time.time() - start
#
# start = time.time()
# flask_logger.error("Hello World")
# print time.time() - start
#
# start = time.time()
# with open('temp', mode='w') as f:
#     f.write('Hello World')
# print time.time() - start