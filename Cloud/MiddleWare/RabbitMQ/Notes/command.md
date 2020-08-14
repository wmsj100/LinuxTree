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
- `rabbitmqctl set_permission -p vhost1 vuser1 '.*' '.*' '.*'` 设置用户的权限
- `rabbitmqctl delete_user vuser1`
- `rabbitmqctl delete_vhost vhost1`
- `rabbitmqctl delete_queue queue_name` 删除队列和队列的消息
- `rabbitmqctl purge_queue queue_name` 删除队列的消息，但队列会保存
- `rabbitmqctl set_user_tags vuser1 administrator` 设置用户的权限
- `rabbitmqctl list_bindings` 列出所有的绑定信息
- `rabbitmqctl list_bindings -p vhost_user1` 列出指定vhost的bind信息

## 参考

