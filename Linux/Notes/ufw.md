---
title: ufw
date: 2020-03-06 22:04:33
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# ufw

## 概要

- ufw是ubuntu默认安装的防火墙工具

## 常用

- `sudo apt install ufw`
- `sudo ufw enable` 开机自动启动防火墙
- `sudo ufw default deny` 关闭所有外部对本机的访问
- `sudo ufw status` 查看当前的防火墙设置
- `sudo ufw allow 22/tcp`
- `sudo ufw allow 45`
- `sudo ufw allow from 192.168.0.103` 允许该ip访问所有端口
- `sudo ufw allow 7100:7200/tcp` 运行端口范围,必须指定tcp/udp协议
- `sudo ufw allow from 192.168.1.0/24 to any port 3306` 允许从192.168.1.1-254网段到服务器3306端口访问.
- `sudo ufw deny from 192.168.1.0/24` 拒绝该网段的所有连接
- `sudo ufw deny from 192.168.1.0/24 to any port 80` 拒绝访问80端口
- `sudo ufw deny from 192.168.1.0/24 to any port 443` 拒绝访问443端口
- `sudo ufw delete allow 22` 删除对22端口的开放
- `sudo ufw delete allow from 192.168.0.106` 删除对ip的开放
```
ubuntu@wmsj100:~/Documents/Github/MyDream/Diary/2020/March$ sudo ufw delete allow 22
Rule deleted
Rule deleted (v6)
ubuntu@wmsj100:~/Documents/Github/MyDream/Diary/2020/March$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
Anywhere                   ALLOW       192.168.0.106
22/tcp (v6)                ALLOW       Anywhere (v6)
```

## 规则

- ufw的默认策略是拦截所有传入的连接,允许所有传出的连接,但服务器上运行的应用和服务却能够对外访问.
- `sudo ufw status numbered` 列出当前规则编号
- `sudo ufw delete 4` 删除
- `sudo ufw disable`禁用ufw
- `sudo ufw reset` 重置

## 参考

- [ubuntu ufw简介](https://blog.csdn.net/Manipula/article/details/91491699)
- [ufw 介绍](https://www.cnblogs.com/xingyunqiu/p/10714905.html)
