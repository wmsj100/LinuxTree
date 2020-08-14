---
title: command
date: 2020-08-14 11:09:35
modify: 
tags: [Notes]
categories: RabbitMQ
author: wmsj100
email: wmsj100@hotmail.com
---

# command

## 概要

- 基础命令

## 命令

- `rabbitmqctl list_users`
- `rabbitmqctl list_queues`
- `rabbitmqctl add_user vuser1 vpwd`
- `rabbitmqctl add_vhost vhost1`
- `rabbitmqctl set_permission `
- `rabbitmqctl delete_user vuser1`
- `rabbitmqctl delete_vhost vhost1`
- `rabbitmqctl delete_queue queue_name` 删除队列和队列的消息
- `rabbitmqctl purge_queue queue_name` 删除队列的消息，但队列会保存

## 参考

