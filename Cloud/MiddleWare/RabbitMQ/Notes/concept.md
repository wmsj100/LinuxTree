---
title: concept
date: 2020-08-14 11:13:09
modify: 
tags: [Notes]
categories: RabbitMQ
author: wmsj100
email: wmsj100@hotmail.com
---

# concept

## 概要

- 基础概念了解

## 概念

- `broker`: 消息队列服务器实体
- `Exchange`: 消息交换机，它指定消息按照什么规则，路由到哪个队列
- `Queue`: 消息队列载体，每个消息都会被投入到一个或多个队列
- `Binding`: 绑定，作用是按照路由规则把Exchange和queue绑定起来
- `Routing key`: 路由关键字，exchange根据这个关键字进行消息投递
- `vhost`: 虚拟主机，一个broker里可以开设很多个vhost，用作不同用户的权限分离
- `producter`: 消息生产者，投递消息的程序
- `consumer`: 消息消费者，接受消息的程序
- `channel`: 通道，在客户端的每个连接里，可以建立多个channel，每个channel代表一个会话任务

## 参考

- [rabbitmq基础](https://www.jianshu.com/p/dae5bbed39b1)
