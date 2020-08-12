---
title: pika
date: 2020-08-12 19:54:56
modify: 
tags: [Basics]
categories: Frame
author: wmsj100
email: wmsj100@hotmail.com
---

# pika

## 概要

- 是用于连接rabbitmq的库

## 范例

```send.py

import pika

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
parameters = pika.ConnectionParameters('rabbit', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='hello body!')
print(' [x] Sent "Hello world" ')
connection.close()
```

```receive.py
import pika

credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
parameters = pika.ConnectionParameters('rabbit', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
print(' [x] Waiting for msg')

channel.start_consuming()
```

## 参考

