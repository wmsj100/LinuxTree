---
title: kernel_ipv4
date: 2020-03-18 21:03:43
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# kernel_ipv4

## 概要

- Ipv4的内核管理功能,这些功能可以阻挡很多网络攻击.
- 这是内核的网络功能,所以相关的设置数据都放在`/proc/sys/net/ipv4/`这个目录内.

## tcp_syncookies

- 这个模块是用来防御DDOS的攻击的,
- DDOS攻击就是客户端发送大量的SYN服务器请求,然后服务器返回SYN确认信息后被客户端直接丢弃,服务器一直在等待客户端回应,这样导致端口被占用,当客户端在发起请求时候服务器就得启动新的端口来应答,这样结果就是服务器端口被耗尽,服务器挂机.
- 这个模块就是在服务器启动随机连接端口(1024:65535)即将用完的时自动启动
- 当启动SYN Cookie时,主机发送SYN/ACK确认数据前,会要求Client端在短时间内回复一个序号,这个序号包含许多原SYN数据包内的信息,包括IP/port等.若Clinet端可以回复正确的序号,那么主机就认为该数据包为可信的.因此会发送SYN/ACK数据包,否则就不理会此数据包.
- 通过这一机制可以大大降低无效的SYN等待端口,避免SYN FLooding的DOS攻击.
- `echo 1 > /proc/sys/net/ipv4/tcp_syncookies` 即可启动该模块
- 这个设置由于违反TCP的三次握手,(因为主机在发送SYN/ACK之前需要先等待Client的序号响应),所以可能会造成某些服务的延迟现象.
- 这个不适合用在负载已经很高的服务器上面,因为负载太高的主机有时会让内核误判遭受SYN Flooding的攻击.

## icmp_echo_ignore_broadcasts

- 阻断式服务常见的是SYN Flooding,不过还有Ping Flooding,就是大量的主机通过发送大容量和大数量的ping请求时,此时主机的带宽可能会被吃光,或者系统可能会宕机.
- 只能取消ICMP类型8的数据包回应,
- 内核取消回应的设置有俩个,
	- icmp_echo_ignore_broadcasts: 仅有在ping broadcast地址时才取消ping的回应,系统默认开启
	- icmo_echo_ignore_all: 全部ping都不回应 系统默认关闭

## /proc/sys/net/ipv4/conf/网络接口

- Linux内核还可以针对不同的网络接口进行不一样的参数设置.
- 网络接口的参数设置存放在`/proc/sys/net/ipv4/conf/`
- 每个接口都以接口代号作为其代表
- 所有这些配置都可以通过`echo 1 > ...`这样来开启,但还是建议修改配置文件`/etc/sysctl.conf`

## 参考

