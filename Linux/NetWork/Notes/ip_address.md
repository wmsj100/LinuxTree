---
title: ip_address
date: 2020-03-09 10:11:01
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# ip_address

## 概要

- iproute2工具包的命令

## 常用命令

- `ip address show` 查看当前所有网络设备,展示包括ip和子网信息
- `ip address show wlan0` 展示wlan0设备信息
- `ip address add 192.168.10.1/24 broadcast 192.168.10.255 dev eth0` 给网卡eth0添加地址并且指定子网和广播地址
	- 通过这个命令可以很容易给一个网卡挂载多个地址
	- eth0虽然没有连接网线,但是正是存在,可以走内部流量
- `ip address del 192.168.10.2/24 dev eth0` 删除网卡的指定ip
- `ip address flush dev eth0` 一次性删除eth0网卡的所有ip

## 参考

