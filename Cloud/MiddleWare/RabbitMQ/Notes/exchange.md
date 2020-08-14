---
title: exchange
date: 2020-08-14 16:36:37
modify: 
tags: [Notes]
categories: RabbitMQ
author: wmsj100
email: wmsj100@hotmail.com
---

# exchange

## 概要

- exchange主要是交换协议，用于处于producer生成的消息要发送到哪个queue队列上。
- fanout是转发消息到当前的所有队列上面
- direct是转发到指定的routing_key的queue上
- topic是转发到匹配的routing_key上面

## 参考

- [rabbitmq exchange](https://www.jianshu.com/p/5ef916009a7f)
