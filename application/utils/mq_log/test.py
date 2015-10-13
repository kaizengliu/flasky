# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/13 15:13

import logging
import unittest
import pika

from mqhandler import MQHandler


class TestMQHandler(unittest.TestCase):
    def setUp(self):
        logger = logging.getLogger("log_use_mq_handler")
        mq_handler = MQHandler("10.209.68.178",
                               5672,
                               'less',
                               'asdfjkl',
                               exchange='mq_log',
                               virtual_host='vn1',
                               machine_id='nx',
                               process_id='flasky')

        formatter = logging.Formatter('%(message)s')
        mq_handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(mq_handler)

        self.logger = logger
        self.mq_handler = mq_handler

        # log client connection
        credentials = pika.PlainCredentials("less", "asdfjkl")
        conn_params = pika.ConnectionParameters(host="10.209.68.178",
                                                port=5672,
                                                virtual_host="vn1",
                                                credentials=credentials)

        connection = pika.BlockingConnection(conn_params)
        channel = connection.channel()

        channel.exchange_declare(exchange="mq_log", type="topic")

        routing_key = "nx.flasky.*"
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange="mq_log",
                   queue=queue_name,
                   routing_key=routing_key)

        self.channel = channel
        self.queue_ame = queue_name

    def tearDown(self):
        self.mq_handler.close()

    def test_func(self):
        msg_send = 'Hello World!'

        self.msg_num = 100

        for i in range(self.msg_num):
            self.logger.error(msg_send)

        def callback(ch, method, properties, body):
            self.assertEqual(msg_send, body.strip())
            self.msg_num -= 1

            if self.msg_num == 0:
                self.channel.close()

        self.channel.basic_consume(callback,
                                   queue=self.queue_ame,
                                   no_ack=True)

        self.channel.start_consuming()


if __name__ == '__main__':
    unittest.main()