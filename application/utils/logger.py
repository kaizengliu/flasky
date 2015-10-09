# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/09 14:57


import logging


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

logger = logging.getLogger('main')

logger.info('dfd')

sh = logging.StreamHandler()
fm = ColoredFormatter("%(asctime)s\t%(process)d|%(thread)d\t%(levelname)s\t%(module)s\t%(funcName)s:%(lineno)d\t%(message)s", "%Y-%m-%d@%H:%M:%S")

sh.setFormatter(fm)

logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

import cStringIO

str_buffer = cStringIO.StringIO()

buffer_handler = logging.StreamHandler(stream=str_buffer)
