---
title: ifconfig
date: 2020-03-09 09:17:14
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# ifconfig

## 概要

- linux老旧的网络管理工具

## 使用

```
ubuntu:/var/log$ ifconfig eth0
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.0.13  netmask 255.255.240.0  broadcast 172.17.15.255
        inet6 fe80::5054:ff:fe2b:57e2  prefixlen 64  scopeid 0x20<link>
        ether 52:54:00:2b:57:e2  txqueuelen 1000  (Ethernet)
        RX packets 7003604  bytes 3061065331 (3.0 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 6481774  bytes 2598234693 (2.5 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
- UP: 网卡是激活状态
- BROADCAST: 支持广播
- RUNNING: 网卡的网线被连接上
- MULTICAST: 支持组播
- mut: 最大传输单元
- innet: ipv4的ip地址
- netmask: 子网掩码
- broadcast: 广播地址
- inet6: ipv6地址
- RX: 表示网络启用到现在的封包接受情况(Receive)
- TX: 表示网络从启用到现在传送情况(Transmit)
- dropped: 表示丢弃的包数量
- overruns: 表示接收时因过速而丢失的数据包数
- frame: 发生frame错误而丢失的数据包数
- collisions: 发送冲突信息包数

- ifconfig eth0

## 参考

- [ifconfig](https://www.cnblogs.com/0to9/p/9591315.html)
