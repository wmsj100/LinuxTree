---
title: ip_static
date: 2020-03-14 23:06:51
modify: 
tags: [Notes]
categories: RaspberryPi
author: wmsj100
email: wmsj100@hotmail.com
---

# ip_static

## 概要

- 树莓派默认是通过wifi连接并且通过dhcp的方式进行动态ip分配
- 如果想同时分配一个静态ip用于本地连接呢

## 分配静态ip

- `sudo vi /etc/dhcpcd.conf`
```
# Example static IP configuration:
#interface eth0
#static ip_address=192.168.0.10/24
#static ip6_address=fd51:42f8:caae:d92e::ff/64
#static routers=192.168.0.1
#static domain_name_servers=192.168.0.1 8.8.8.8 fd51:42f8:caae:d92e::1
interface enxb827eb188850
static ip_address=192.168.20.2/24
```
- `interface enxb...`选择要设置的接口
- `static ip_address=192.168.20.2/24` 选择ip和子网
- `sudo /etc/init.d/networking restart` 重启网卡

## 参考

