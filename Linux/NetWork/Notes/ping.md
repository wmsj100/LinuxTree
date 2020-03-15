---
title: ping
date: 2020-03-15 14:43:55
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# ping

## 概要

- 测试网络是否连同,请求是否可以到达

## 使用

- 参数介绍
	- c ping的次数
	- n 输出数据时不进行IP与主机名的反查
	- s 发送出去的ICMP数据包的大小,默认是56byte
	- t TTL的数值,默认是255,每经过一个节点减少1
	- W 等待响应对方主机的秒数
	- M do|done 主要在检测网络的MTU数值大小,
		- do 代表传送一个DF(Don't Fragment) 标志,让数据包不能重新拆包与打包
		- done 代表不要传送DF标志,数据包可以在其他主机上拆包和打包

- `ping -c 2 baidu.com` 发送俩次请求
- `ping -s 1000 -c 5 -M do 192.168.20.1`
```
pi@raspPI:~ $ ping -s 1300 -c 5 -M do 192.168.20.1
PING 192.168.20.1 (192.168.20.1) 1300(1328) bytes of data.
1308 bytes from 192.168.20.1: icmp_seq=1 ttl=64 time=0.774 ms
1308 bytes from 192.168.20.1: icmp_seq=2 ttl=64 time=0.668 ms
```

## 参考

