# -*-coding: utf-8-*-
# time: 2015/09/23 08:20
# author: liukaizeng

from base import *

DEBUG = True

SERVER_NAME = 'lkz.com:5000'

EMAIL_HOST = 'smtp.126.com'
EMAIL_PORT = 25
EMAIL_USE_TLS = True
EMAIL_TIME_OUT = 10
EMAIL_HOST_USER = 'liukaizeng1111@126.com'
EMAIL_HOST_PASSWORD = 'fcepstxvrhxxptlh'

REDIS_HOST = '10.209.68.178'
REDIS_PORT = 6379

DB = {
    'host': '10.209.68.178',
    'port': 3306,
    'user': 'lkz',
    'password': 'asdfjkl;',
    'db_name': 'blog'
}

# REDIS_HOST = '192.168.199.191'
# REDIS_PORT = 6379
#
# DB = {
#     "host": '192.168.199.191',
#     "port": 3306,
#     "db_name": 'blog',
#     "user": 'blog',
#     "password": 'blog'
# }


# machine name, used to identity different machines
MACHINE = "nx"

# machine name, used to identity different processes
PROCESS = "flasky"

AMQP_HOST = "10.209.68.178"
AMQP_PORT = 5672
AMQP_VIRTUAL_HOST = "vn1"
AMQP_USER_NAME = 'less'
AMQP_PASSWORD = 'asdfjkl'
AMQP_EXCHANGE = "mq_log"
