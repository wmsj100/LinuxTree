---
title: DDoS
date: 2020-03-16 15:11:59
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# DDoS

## 概要

- DDoS: Distributed Denial of Service 分布式拒绝服务攻击
- 它是通过分散在世界各地的僵尸计算机进行攻击,让系统提供的服务被阻断而无法顺利地为其他用户提供服务.
- 攻击方式有很多种,最常见的就是SYN Flood攻击法
- 但主机受到一个带有SYN的TCP请求之后,就会启用对方要求的port来等待连接,并且发送出回应数据报(带有SYN/ACK标志的TCP数据包)等待Client回应
- 如果Client在发送出SYN的数据包后,却将来自服务器的确认数据包丢弃,那么Server端就会一直空等,
- 而Client端可以通过软件功能,在短时间内持续发出这样的SYN数据包,那么Server就会持续不断的发送确认数据包,并且开启大量的port在空等.
- 等到全部port都启用完毕,那么系统就挂了
- 这种方式是为了让系统无法提供正常服务.

## 参考

