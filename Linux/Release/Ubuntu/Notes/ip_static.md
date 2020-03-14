---
title: ip_static
date: 2020-03-14 23:17:59
modify: 
tags: [Notes]
categories: Ubuntu
author: wmsj100
email: wmsj100@hotmail.com
---

# ip_static

## 概要

- ubuntu设置静态IP

## 配置

- `sudo vi /etc/network/interfaces`
```
auto enp2s0
iface enp2s0 inet static
address 192.168.20.1
netmask	255.255.255.0
gateway	192.168.20.1
```
- 分别按照上面的配置进行

## 参考

