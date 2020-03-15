---
title: host
date: 2020-03-15 22:17:43
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# host

## 概要

- 这个和hostname并没有关系,它是用来通过dns的配置来查询域名和ip的对应关系的.

## 使用

- `host -a www.google.com`
- `host www.google.com`
```
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/NetWork/Notes$ host www.google.com
www.google.com has address 69.171.235.101
www.google.com has IPv6 address 2404:6800:4012:1::2004
```
- 现在通常使用`dig`替代使用`host/nslookup`
- `nslookup 69.171.235.101`	可以通过ip来反向解析域名,但经常会失败
- `nslookup www.google.com`
```
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/NetWork/Notes$ nslookup www.google.com
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	www.google.com
Address: 69.63.181.11
Name:	www.google.com
Address: 2001::45ab:f841
```

## 参考

