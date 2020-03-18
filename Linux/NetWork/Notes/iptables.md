---
title: iptables
date: 2020-03-17 12:32:48
modify: 2020-03-18 16:42:31  
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# iptables

## 概要

- netfilter/iptables(简称iptables)组成Linux平台下的包过滤防火墙,它可以替代商业防火墙解决方案,完成封包过滤/封包重定向和网络地质转换(NAT)等功能
- 基础就是内部有很多表,每个表有很多rule

## 基础

- 规则(rules)其实就是网络管理员预定以的条件,规则一般的定义为"如果数据包头符合这样的条件,就这样处理这个数据包"
- 规则存储在内核空间的信息包过滤表中,
- 这些规则分别指定了源地址/目的地址/传输协议(TCP/UDP/ICMP)和服务类型(HTTP/FTP/SMTP)
- 当数据包和规则匹配时,iptables就根据规则所定义的方法来处理这些数据包,如放行(accept)/拒绝(reject)/丢弃(drop)等.
- 配置防火墙的主要工作就是添加/修改和删除这些规则.

## 参数解析

- t 后接table; filter/nat/mangle
- L 列出目前的table的规则
- n 不进行IP和HOSTNAME的反查,显示信息的速度会快很多
- v 列出更多信息,
- F 清除所有已制定规则
- X 清除所有用户自定义的table
- Z 将所有的table的计数与流量统计都归零
---
- 定义默认策略
- P INPUT/OUTPUT/FORWARD
	- `sudo iptables -t filter -P INPUT DROP` 所有进入的流量全部扔掉
	- `sudo iptables -t filter -P OUTPUT ACCEPT` 所有出的流量全部放行
	- `sudo iptables -t filter -P FORWARD ACCEPT` 所有转发的流量全部放行
---
- 数据包的基础比对
- AI 链名: 针对某条链进行规则的"插入"或"累加"
	- A: 新增加一条规则,该规则增加在原规则的最后面
	- I: 插入一条规则,如果不制定此规则的顺序,默认第一条
- io 网络接口: 设备数据包进出的接口规范
	- i: 数据包进入的那个网络接口
	- o: 数据包出去的那个网络接口
- p 协定: tcp/udp/icmp/all
- s 来源IP/网络
	- IP: 192.168.0.100
	- 网络: 192.168.0.0/24 192.168.0.0/255.255.255.0 均可
	- ! 不许
- d 目标IP/网络
- j ACCEPT/REJECT/DROP/LOG
- `iptable [-AI 链] [-io 网络接口] [-p tcp,udp] [-s 来源IP/网络] [--sport 端口范围] [-d 目标IP/网络] [--dport 端口范围] -j [ACCEPT/REJECT/DROP/LOG]
	- --sport 来源的端口范围,可以是连续的 1024:65535
	- --dport 目标的端口范围
	- 只有tcp/udp数据有端口,因此如果要限制端口,必须要通过-p来指定协议
- --syn 针对TCP的请求可以设置这个参数,表示主动请求时候的处理过程

```
pi@raspPI:~ $ sudo iptables -t filter -L -n
Chain INPUT (policy ACCEPT)
target     prot opt source               destination

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```
- target: 代表进行的操作,ACCEPT是放行,REJECT是拒绝,DROP就是丢弃
- prot: 代表使用的数据包协议,主要有TCP/UDP/ICMP三种
- opt: 额外的选项说明
- source: 此规则是针对哪个源IP进行限制
- destination: 此规则是针对那个目标IP进行限制

## 建议

- 在重新制定防火墙规则时将所有规则清除.

## 常用

- `sudo iptables -L -n` 查看当前的表规则
- `sudo iptables -F / -X / -Z` 三条命令分开输入,可以清空并重置iptables规则,默认是全部accept
- `sudo iptable-save -t filter` 列出完整的防火墙规则
- `sudo iptables -P FORWARD ACCEPT` 设置转发的流量全部放行
- `sudo iptables -A INPUT -i enxb827eb188850 -s 192.168.0.101 -j LOG` 对网络段的访问记录到/var/log/messages
- `sudo iptables -A INPUT -i enxb827eb188850 -s 192.168.20.0/24 -j ACCEPT` 信任网络段
- `sudo iptables -A INPUT -i enxb827eb188850 -s 192.168.50.0/25 -j DROP` 屏蔽网络段
- `sudo iptables -A INPUT -i enxb827eb188850 -p tcp -s 192.168.0.101/24 --sport 1024:65534 --dport ssh -j DROP` 只要是来自192.168.0.101/24这个IP的且端口在1024-65534范围内且请求本机ssh的22端口的全部丢弃
- `sudo iptables -A INPUT -i enxb827eb188850 -p tcp --sport 1:1023 --dport 1:1023 --syn -j DROP` 表示所有来自远端的且请求端口小于1024的,访问的目标端口小于1024的主动发起的连接请求全部丢弃

## 参考

- [iptables 讲解](https://www.jianshu.com/p/ee4ee15d3658)
