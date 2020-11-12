---
title: storage_process
date: 2020-11-12 09:30:12
modify: 
tags: [Notes]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# storage_process

## 概要

- mysql也支持存储过程
- 存储过程是预编译的sql代码，用于处理数据
- 存储过程有一下几个优点：
	- 执行速度快，可以减少很多的T-sql流量
	- 减少网络传输
	- 避免sql注入
	- 减少业务中的重复编写，类似编程语言的面向对象编程
	- 可以在多个语言和多平台中提高同一调用
	- 修改不会影响业务，不需要修改业务代码
	- 语法标准，DBA可以直接修改
- 缺点：
	- 如果有大量的频繁调用，会增加数据库的服务器压力

## 总结

- 很多业务代码其实只是对于数据的整理和处理
- 尤其是通过多个表组合来获取数据，可以通过存储过程来实现，而不是全部都在业务端来实现
- 存储过程也是编程范畴

## 参考

- [mysql 存储过程](https://www.cnblogs.com/jiangxiaobo/p/7448854.html)
