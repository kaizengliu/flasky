# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/12 15:38

import pika

from logging import Handler

try:
    unicode
    _unicode = True
except NameError:
    _unicode = False


class MQHandler(Handler):
    def __init__(self, host, port, user, password, exchange="mq_log", virtual_host="/", machine_id=None, process_id=None):
        Handler.__init__(self)

        self.machine_id = machine_id
        self.process_id = process_id
        self.exchange = exchange

        credentials = pika.PlainCredentials(user, password)

        __conn_params = {
            "host": host,
            "port": port,
            "virtual_host": virtual_host,
            "credentials": credentials
        }

        self.__conn = None
        self.__channel = None
        self.__conn_params = pika.ConnectionParameters(**__conn_params)

    def get_connection(self):
        conn = pika.BlockingConnection(self.__conn_params)

        return conn

    def get_channel(self):
        if not self.__conn:
            self.__conn = self.get_connection()

        channel = self.__conn.channel()
        channel.exchange_declare(exchange=self.exchange, type="topic")

        channel.confirm_delivery()

        return channel

    def publish_msg(self, routing_key, msg):
        # 现在没有找到刷新消息到rabbitmq server的方法，所以暂时使用
        # channel.close()方法来刷新消息. 再次发送消息时，需要重新建立channel

        if not self.__channel:
            self.__channel = self.get_channel()

        ret = self.__channel.basic_publish(exchange=self.exchange,
                                           routing_key=routing_key,
                                           body=msg)
        if not ret:
            print 'Message %s could not be confirmed' % msg

    def generate_routing_key(self, level):
        return ".".join([self.machine_id or "*", self.process_id or "*", level])

    def handleError(self, record):
        if self.__conn and self.__conn.is_open:
            self.__conn.close()
            self.__conn = None

        Handler.handleError(self, record)

    def emit(self, record):
        try:
            level = record.levelname
            routing_key = self.generate_routing_key(level)
            msg = self.format(record)

            fs = "%s\n"
            if not _unicode: #if no unicode support...
                self.publish_msg(routing_key, msg)
            else:
                self.publish_msg(routing_key, fs % msg.encode("UTF-8"))
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        self.acquire()
        try:
            if self.__conn and self.__conn.is_open:
                self.__conn.close()
                self.__conn = None
        finally:
            self.release()

        Handler.close(self)
