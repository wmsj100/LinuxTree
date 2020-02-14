---
title: netstat
date: 2019-04-09 13:02:57	
modify: 2020-02-13 22:53:32 
tag: [Basic]
categories: Linux 
author: wmsj100
mail: wmsj100@hotmail.com
---

# netstat

## 概述
- 这个命令是用来查看端口占用情况的

## 使用
- netstat -tlnp 查看端口占用
[root@iZ2ze1u9ywulp4snxg73lpZ home]# netstat -tlnp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      4936/sshd
tcp        0      0 0.0.0.0:3306            0.0.0.0:*               LISTEN      27839/mysqld

可以看到mysql的3306端口已经开始监听
- `sudo lsof -i :80` 查看80端口被那个程序占用
COMMAND  PID     USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1158     root    8u  IPv4  20069      0t0  TCP *:http (LISTEN)
nginx   1158     root    9u  IPv6  20070      0t0  TCP *:http (LISTEN)
nginx   5317 www-data    8u  IPv4  20069      0t0  TCP *:http (LISTEN)
nginx   5317 www-data    9u  IPv6  20070      0t0  TCP *:http (LISTEN)


## 参考
- [netstat](https://baijiahao.baidu.com/s?id=1622422454033168404&wfr=spider&for=pc)
