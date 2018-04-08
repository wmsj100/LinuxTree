---
title: 安装mysql
date: Tue 05 Dec 2017 11:56:07 PM CST
tag: [mysql]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- yum install mariadb mariadb-server 安装
- systemctl star mariadb 安装完成后启动mariadb
- systemctl enable mariadb 设置开机启动
- mysql_secure_installation 进行简单的mysql配置
- grant all on *.* to wmsj100@localhost identified by "wmsj100" 创建一个有任何权限的用户
