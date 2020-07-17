---
title: connect
date: 2020-07-17 11:17:21
modify: 
tags: [Notes]
categories: Oracle
author: wmsj100
email: wmsj100@hotmail.com
---

# connect

## 概要

- oracle的连接需要通过服务名来连接

## 操作

- `show parameter service_name`获取到服务名
- `cx_Oracle(user, passwd, host/service_name)` 通过这样的方式来连接数据库

## 参考

- [oracle 服务名](https://www.cnblogs.com/zmlctt/p/3755957.html)
