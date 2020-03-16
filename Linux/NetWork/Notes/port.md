---
title: port
date: 2020-03-06 21:28:48
modify: 
tags: [March]
categories: 2020
author: wmsj100
email: wmsj100@hotmail.com
---

# port

## 概要

- 主要用来进行通信,一个ip绑定有多个port
- `/etc/services` 保存有所有的约定俗成的端口号
- `cat /proc/sys/net/ipv4/ip_local_port_range` 32768	60999 查看当前主机的可用的端口
- 服务端的port是固定的,提供client来访问
- client访问服务的时会随即启动一个大于1024的端口访问服务端
- tcp的port的长度时16,所以可以开启的最大的port值时2^16=65536
- 但所有的port端都占满之后就没有端口可开了,此时服务器就挂了.
- 开启的服务是运行在内存中的
- 开启服务占用的端口是可以穿过防火墙的,所以防火墙对于这些端口而言是不存在的.只能是在添加一些关于mac或者指定ip值的过滤条件

## 常用工具

### nmap

- nmap 可以查看当前主机开放的端口
- `nmap localhost`
```
(virtualenv) pi@raspberrypi:~ $ nmap 192.168.0.102
Starting Nmap 7.70 ( https://nmap.org ) at 2020-03-06 21:37 CST
Nmap scan report for 192.168.0.102
Host is up (0.00052s latency).
Not shown: 994 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
5900/tcp open  vnc
8001/tcp open  vcom-tunnel
8002/tcp open  teradataordbms
8010/tcp open  xmpp
```

### netstat

- netstat查看当前的端口占用情况
```
(virtualenv) pi@raspberrypi:~ $ netstat -nltp
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 192.168.0.102:7946      0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:8010            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:5900            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:16062           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:8001            0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:8002            0.0.0.0:*               LISTEN      -
tcp6       0      0 :::5900                 :::*                    LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
```

### lsof

- lsof查看具体端口被占用详情
```
(py3env) ubuntu:~$ sudo lsof -i :3306
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
mysqld  1251 mysql   30u  IPv4  21861      0t0  TCP localhost.localdomain:mysql (LISTEN)
```

### netcat

- 查看端口占用
```
(py3env) ubuntu:~$ nc -vv localhost 8080
nc: connect to localhost port 8080 (tcp) failed: Connection refused
(py3env) ubuntu:~$ nc -vv localhost 8006
Connection to localhost 8006 port [tcp/*] succeeded!
```

## 参考

- [端口常用工具解析](https://blog.csdn.net/appleyuchi/article/details/80188843)
