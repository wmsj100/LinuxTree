---
title: 给arch主机指定静态ip
date: 2020-03-14 18:15:49
modify: 
tags: [Summary]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# 给arch主机指定静态ip

## 概要

- 之前总觉得ip神奇的不行,而且觉得ip必须要通过dhcp的方式来指定才可以
- 之前尝试过用static方式指定的ip可以ping同局域网主机,但是dns无法获取,如果我直接`ping baidu.com`,它是返回失败的
- 这种情况说明路由设置有问题
- 局域网可以通信说明是直接通过主机=主机的方式的,没有经过路由,所以不配置默认路由网关也可以访问
- 也就是说直接同一根网线把俩台主机连接起来也是可以访问的,只要设置相应的ip就可以.

## 配置操作

- `sudo ip link set eth0 up`
- `sudo ip addr add 192.168.0.108/24 broadcast 192.168.0.255 dev eth0` 给网卡绑定ip
	- 此时已经可以访问局域网的主机了,只要提前知道其他主机ip
	- 这样的访问是主机到主机的,不经过路由器的
	- `ping baidu.com`会提示network不可达,因为当前流量只是再局域网内的
- `sudo ip route add default via 192.168.0.1 dev eth0` 添加默认路由到路由器的网关
- `vi /etc/resolv.conf` 查看dns是否有同步过来,这个通过过程是自动的
```
# Generated by resolvconf
nameserver 192.168.1.1
nameserver 192.168.0.1
```
- 然后就可以访问互联网了
- `ping baidu.com`

## 测试

- 我刚刚用电脑直接通过网线连接了树莓派,分别给俩台设备手动设置ip
- `sudo ip addr add 192.168.20.1/24 broadcast 192.168.20.255 dev eth0` 电脑
- `sudo ip addr add 192.168.20.2/24 broadcast 192.168.20.255 dev eth1` 树莓派
- `ip route` 查看路由都有自动添加设备,
- `ip link show` 俩台设备的网卡都有启动
- `ping 192.168.20.1` 是可以ping通的,网线的灯一直在闪烁.
- `ip neith` 查看当前局域网的arp,会发现俩台设备都已经添加好了.
- 这样就和树莓派组建了一个局域网,

## 总结

- 其实局域网内部的通信是通过arp来确认ip和mac地址的,确认之后是不经过路由器的,是主机之间直接通信的
- 一张网卡可以绑定多个ip

## 参考

