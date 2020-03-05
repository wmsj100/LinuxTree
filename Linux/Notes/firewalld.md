---
title: firewalld
date: 2020-03-05 10:18:35
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# firewalld

## 概要

- centos7之前默认的防火墙软件是iptables,之后版本就默认成了`firewalld`
- 默认是关闭所有的端口接入的，可以请求端口，但是不能通过端口接入

## 常用命令

- `sudo firewall-cmd --get-zone-of-interface=wlp3s0` 查看当前网卡/接口所属的域，默认返回`public`
- `sudo firewall-cmd --zone=public --list-ports` 查看当前域开发的端口，默认是空
- `sudo firewall-cmd --zone=public --add-port=2377/tcp --permanent` 给public域添加端口白名单，通过设置permanent来让设置持久化，否则重启firewall就失效了
- 再次查看public域开发的端口就会发现已经有一个端口开发了

## 参考

- [centos firewall常用操作](https://www.cnblogs.com/inos/p/10985042.html)
