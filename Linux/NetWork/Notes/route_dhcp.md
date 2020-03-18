---
title: 动态路由
date: 2020-03-18 12:10:56
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# 动态路由

## 概要

- 通常路由的变更是需要去路由器设置,是一个手动的过程
- 如果涉及到路由转发,首先需要判断当前路由设备的路由转发功能有没有开启
- `cat /proc/sys/net/ipve/ip_forward` 如果为1表示开启了.
- `vi /etc/sysctl.conf` 如果要开启需要修改这个配置文件
- 如果路由转发需要实现,就得在俩个路由都要添加关于路由的转发接口,这样有可能会出错或遗漏导致转发不成功.
- 通常通过软件来实现这个动作,
- `sudo apt install quagga` 这个软件可以实现路由的动态监听
- 该软件是在zebra的基础上开发的,所以需要先配置zebra
- 所有的配置文件都放在`/etc/quagga`目录,以.conf结尾
- zebra的配置
```
hostname www.centos.vbird
password linuxpi
enable password linuxpi
log file /var/log/quagga/zebra.log
```
- riqd.conf
```
hostname www.centos.vbird
password linuxpi
debug rip events
debug rip packet
router rip
version 2
network 192.168.20.0/24
network 192.168.0.0/24
network 192.168.100.0/24
interface wlx081079db1327
no ip rip authentication mode
log file /var/log/quagga/zebra.log
```

## 参考

