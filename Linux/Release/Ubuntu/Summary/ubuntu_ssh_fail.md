---
title: ssh到ubuntu主机失败
date: 2020-03-07 09:35:05
modify: 
tags: [Summary]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# ssh到ubuntu主机失败

## 概要

- 电脑新装了ubuntu,配置也好了,但通过树莓派无法ssh登陆,一直报forbiden,不明白什么原因

## 解决

- `nmap localhost`看到22端口没有开放,应该是22端口的应用没有启用
- 查找网络资料说是openssh-server没有安装
- `sudo apt install openssh-server`提示openssh-client冲突
- `sudo apt remove openssh-client`
- `sudo apt install openssh-server`
- `map localhost`
```
Starting Nmap 7.60 ( https://nmap.org ) at 2020-03-07 09:37 CST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000078s latency).
Not shown: 998 closed ports
PORT    STATE SERVICE
22/tcp  open  ssh
631/tcp open  ipp

Nmap done: 1 IP address (1 host up) scanned in 0.05 seconds
```
- 看到端口已经启用了
- 防火墙放开端口
- `sudo ufw allow 22`
- 然后pi通过ssh登陆ubuntu成功

## 参考

- [ubuntu ssh无法访问](https://blog.csdn.net/anlu0/article/details/91635496)
