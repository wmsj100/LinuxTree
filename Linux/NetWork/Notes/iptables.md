---
title: iptables
date: 2020-03-17 12:32:48
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# iptables

## 概要

- netfilter/iptables(简称iptables)组成Linux平台下的包过滤防火墙,它可以替代商业防火墙解决方案,完成封包过滤/封包重定向和网络地质转换(NAT)等功能

## 基础

- 规则(rules)其实就是网络管理员预定以的条件,规则一般的定义为"如果数据包头符合这样的条件,就这样处理这个数据包"
- 规则存储在内核空间的信息包过滤表中,
- 这些规则分别指定了源地址/目的地址/传输协议(TCP/UDP/ICMP)和服务类型(HTTP/FTP/SMTP)
- 当数据包和规则匹配时,iptables就根据规则所定义的方法来处理这些数据包,如放行(accept)/拒绝(reject)/丢弃(drop)等.
- 配置防火墙的主要工作就是添加/修改和删除这些规则.
## 参考

