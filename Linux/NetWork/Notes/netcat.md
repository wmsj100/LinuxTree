---
title: netcat
date: 2020-03-16 12:07:41
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# netcat

## 概要

- nc,有些系统改名为netcat,可以用来作为某些服务的检测
- 可以连接到某个port来进行通信
- 还可以自行启动一个port来监听其他用户的连接.
- 俩台连接的nc端口可以互通信息

## 使用

- `nc -l 20000` 在本机启动一个20000的tcp端口
- `nc -l -u 20000` 启动一个20000的udp端口监听
- `nc localhost 20000` 连接20000的tcp端口
- `nc localhost -u 20000` 连接20000的udp端口
- `nc 192.168.20.2 -u 20000` 通过nc连接目标主机的端口,如果无法连接,大概率是因为端口被防火墙屏蔽了.

## 参考

