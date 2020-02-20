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
- get
	- get webname 查看值
- del
	- del webname 删除值
- ttl
	- ttl webname 查询webname的过期时间，如果已经销毁，返回-2
- keys
	- keys * 查询所有key
	- keys web* 模糊查询，查询key开头的键
- expire 设置过期时间
	- EXPIRE webname 10

## 数据类型

- string 字符串
- hash 哈希值
- list 列表
- set 集合
- zset 有序集合

## 参考

- [redis](https://www.django.cn/article/show-24.html)
