---
title: netstat
date: 2019-04-09 13:02:57	
modify: 
tag: [Basic]
categories: Linux 
author: wmsj100
mail: wmsj100@hotmail.com
---

# netstat

## 概述
- 这个命令是用来查看端口占用情况的

## 使用
- netstat -tlnp
[root@iZ2ze1u9ywulp4snxg73lpZ home]# netstat -tlnp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      4936/sshd
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      27839/mysqld

可以看到mysql的3306端口已经开始监听

## 参考
- [netstat](https://baijiahao.baidu.com/s?id=1622422454033168404&wfr=spider&for=pc)
