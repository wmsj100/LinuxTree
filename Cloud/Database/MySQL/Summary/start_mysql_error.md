---
title: start_mysql_error
date: 2020-05-19 14:55:57
modify: 
tags: [Summary]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# start_mysql_error

## 概要

- mysql通过rpm方式安装完成后执行`systemctl start mysqld.service`启动失败

## 分析

- `mysqld --initialize` 确定数据库是否执行了初始化操作 
- 确定mysql的datadir目录权限是否正确，应该是`mysql:mysql`
- 确定mysql的pid目录权限是否正确`ll /var/run/mysql`
- 查看mysql的日志文件`vi /var/log/mysqld.log`
- 排查磁盘空间是否正常

## 参考

