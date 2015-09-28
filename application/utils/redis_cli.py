# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/28 17:18

import redis

from application.configure import setting

redis_cli = redis.StrictRedis(setting.REDIS_HOST, setting.REDIS_PORT)
