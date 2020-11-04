---
title: celery
date: 2020-11-04 19:10:51
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# celery

## 概要

- celery是分布式管理消息队列的模块
- 该库对于消息通过使用msgpack来压缩消息，要比通常的json字段体积小很多
- 如果报错JSON格式，通常不是因为消息返回的数据格式问题，而很可能是消息的使用问题，自己排查代码逻辑

## 参考

