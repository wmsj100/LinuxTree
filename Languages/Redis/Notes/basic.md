---
title: basic
date: 2020-02-20 19:26:50
modify: 
tags: [Notes]
categories: Redis
author: wmsj100
email: wmsj100@hotmail.com
---

# basic

## 概要

- redis的基础操作

## 安装

- sudo apt instal redis-server
- sudo apt purge --auto-remove redis-server
- sudo service redis-server start

## 基础

- redis的默认配置文件为`/etc/redis/redis.conf`
- `6379` redis的默认端口

## 曾删改查

- set
	- set webname wmsj100.com 不指定过期时间长期有效
	- set webname wmsj100.com ex 10 指定过期时间10s， 10s之后数据被销毁
	- 因为set可以同时追加参数，所以可以替代设置过期时间的，主推用set
- setrange 10 val 在val的所以6之后用val替换，如果val长度小于6，会用0追加前缀。
- get 只处理string类型的值
	- get webname 查看值
- getrange num start end 获取字符串的字串，start和end是位置索引，都包括在内
	- GETRANGE str1 5 10 `"me is "`
- getset num val 重置num的值为val并且返回num之前的值
	- getset num 0 `-10`
- del
	- del webname 删除值
- ttl
	- ttl webname 查询webname的过期时间，如果已经销毁，返回-2
- keys
	- keys * 查询所有key
	- keys web* 模糊查询，查询key开头的键
- expire 设置过期时间
	- EXPIRE webname 10
- append
	- append text 'hello' 追加值
- decr 对数字进行减1操作
	- decr num
- decrby 将key对应的数字减目标值
	- decrby num 10 将num减10
- incr num 对数字加1, 如果num值没有设置，会默认先把num设置为0，然后加1
- incrby num 5 对数字加5，如果num不存在，会先设置为0，然后加5
- increbyfloat num float 设置num和float相加，num可以为整数和浮点数，如果不是数字，会报错
- mget key1 key2 key3 返回全部key的值，如果key不存在，返回nil，所以这个操作从来不会失败，返回的是一个列表
- MSET num3 45 str 'hello str' 同时对多个变量进行赋值操作，总是返回ok，因为不会失败
- MSETNX str 1 num4 34 同时设置多个变量的值，如果一个变量存在就返回失败，要么全部成功，要么全部失败
- PSETEX num4 1000 'hello' 设置值的同时设置过期时间，单位是毫秒

## 数据类型

- string 字符串
- hash 哈希值
- list 列表
- set 集合
- zset 有序集合

## 参考

- [redis](https://www.django.cn/article/show-24.html)
