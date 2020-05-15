---
title: max_connections
date: 2020-05-15 14:18:59
modify: 
tags: [Notes]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# max_connections

## 概要

- mysql的最大并发量是通过这个值来设置的，
- mysql的最小并发是1，最大并发是100,000，默认的并发量是151。

## 查看

- `sudo mysql`
- `show global variables like 'max_connections';`
- `set global max_connections=1000;`
- `show global variables like 'max_connections';`
- 这样的设置只是针对当前，如果mysql重启，该设置丢失
- `vi /etc/mysql/my.cnf`在[mysqld]写入`max_connections=10000`，然后重启mysql

## 参考

- [mysql max_connections](https://www.jianshu.com/p/01351e72e5ce)
