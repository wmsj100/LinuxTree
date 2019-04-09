---
title: 字符集
date: 2019-04-09 21:56:08	
modify: 
tag: [basic]
categories: MySQL 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 字符集

## 概述
- mysql默认是无法插入中文的，因为默认的字符集不是`utf8`
- 首先需要添加utf8的设置

## 配置
- vim /etc/my.cnf
	[mysqld]
	character-set-server=utf8
	[client]
	default-character-set=utf8
	[mysql]
	default-character-set=utf8
- service mariadb restart

- show variables like 'char%'; 查看当前表的字符集
- show create database test \G; 查看创建数据库时候的信息，可以查看到字段`character`
- alter database test character set utf8; 修改数据库字符集为`utf8`
- alter tabel test_student convert to character set utf8; 把表的所有字段都转换为utf8


## 参考
- [中文转换](https://www.cnblogs.com/shootercheng/p/5836657.html)
- [彻底解决中文](https://www.cnblogs.com/jasonzeng/p/8341445.html)
