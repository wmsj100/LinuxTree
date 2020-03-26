---
title: static_ip
date: 2020-03-26 13:21:49
modify: 
tags: [Notes]
categories: ArchLinux
author: wmsj100
email: wmsj100@hotmail.com
---

# static_ip

## 概要

- ArchLinux的网络是通过netctl来管理的,所以所有的网络设置都在它的配置文件中进行配置

## 配置

- netctl的配置文件的模板在example中可以找到
```
Description='A basic static ethernet connection'
Interface=enp5s0
Connection=ethernet
IP=static
Address=('192.168.20.3/24')
#Routes=('192.168.0.0/24 via 192.168.1.2')
#Gateway='192.168.20.1'
DNS=('192.168.20.1')

## For IPv6 autoconfiguration
#IP6=stateless

## For IPv6 static address configuration
#IP6=static
#Address6=('1234:5678:9abc:def::1/64' '1234:3456::123/96')
#Routes6=('abcd::1234')
#Gateway6='1234:0:123::abcd'
```
- `sudo netctl start enp5s0` 就可以了

## 参考

