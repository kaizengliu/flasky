# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/10/12 17:08


import pika

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

i = 1

channel.queue_bind(exchange="mq_log",
                   queue=queue_name,
                   routing_key=routing_key)


def callback(ch, method, properties, body):
    global i
    print body
    print i
    i += 1

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()