---
title: network_error
date: 2020-03-26 13:53:39
modify: 
tags: [Summary]
categories: RaspberryPi
author: wmsj100
email: wmsj100@hotmail.com
---

# network_error

## 概要

- 树莓派之前是通过wifi直接连接路由器来实现上网功能的,现在通过网线连接笔记本
- 在笔记不配置nat,
	- `sudo iptables -t nat -S POSTROUTING -s 192.168.20.0/24 -o wlan0 -j MASQUERADE`
- 在树莓派ping网络,还是失败,
- 查看路由,发现默认路由还是之前的旧的配置
	- `sudo vi /etc/dhcpcd.conf` 添加`static routes=192.168.20.3`
- 然后再试,发现还是无法ping
- 在笔记本查看转发功能是否开启,查看网卡是否启动,查看路由配置是否ok
- 上述修改之后,实现了树莓派的网络功能

## 参考

