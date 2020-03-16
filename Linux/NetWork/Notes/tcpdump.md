---
title: tcpdump
date: 2020-03-16 11:12:51
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# tcpdump

## 概要

- 这是一个抓包工具,可以查看所有流量
- 需要使用sudo权限

## 使用

- nn: 直接以IP即port number显示,而非主机名和服务名称
- i: 要监听的网络接口,eth0/lo/wlan0
- w: 将将监听的数据包存储下来
- r: 从文件读取数据包,这个文件是由-w制作的.
- c: 监听的数量
- host 127.0.0.1 针对单台主机进行数据包捕获
- net 192.168 针对某个网络来进行数据包捕获
- src host 127.0.0.1 添加来源限制
- dst net 192.168  添加目标限制
- tcp port 21 针对通信协议和端口检测 tcp/udp/arp/ether
- and / or 数据包数据的整合显示

## 范例

- `sudo tcpdump -nn -i eth0 arp` 检测eth0网卡上的arp请求
- `sudo tcpdump -nn -i eth0 port 21` 检测eth0上的21端口
- `sudo tcpdump -nn -i eth0 port 22 and src host 192.168.20.2` 监听eth0的22端口,且数据源来自192.168.20.2

## tcpdump 数据结构解析

```
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/Release/ArchLinux/Notes$ sudo tcpdump -nn -i enp2s0 port 22 and dst host 192.168.20.2
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on enp2s0, link-type EN10MB (Ethernet), capture size 262144 bytes
11:33:48.504539 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [P.], seq 2600519776:2600519812, ack 3774766040, win 501, options [nop,nop,TS val 2971323152 ecr 164309696], length 36
11:33:48.505721 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [.], ack 37, win 501, options [nop,nop,TS val 2971323154 ecr 164329176], length 0
11:33:48.656187 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [P.], seq 36:72, ack 37, win 501, options [nop,nop,TS val 2971323304 ecr 164329176], length 36
11:33:48.657028 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [.], ack 73, win 501, options [nop,nop,TS val 2971323305 ecr 164329327], length 0
11:33:48.760706 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [P.], seq 72:108, ack 73, win 501, options [nop,nop,TS val 2971323409 ecr 164329327], length 36
11:33:48.761620 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [.], ack 109, win 501, options [nop,nop,TS val 2971323410 ecr 164329432], length 0
11:33:48.856631 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [P.], seq 108:144, ack 109, win 501, options [nop,nop,TS val 2971323505 ecr 164329432], length 36
11:33:48.857533 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [.], ack 145, win 501, options [nop,nop,TS val 2971323505 ecr 164329528], length 0
11:33:57.816517 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [P.], seq 144:180, ack 145, win 501, options [nop,nop,TS val 2971332464 ecr 164329528], length 36
11:33:57.818919 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [.], ack 181, win 501, options [nop,nop,TS val 2971332467 ecr 164338489], length 0
11:33:57.824092 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [.], ack 249, win 501, options [nop,nop,TS val 2971332472 ecr 164338494], length 0
11:33:57.825873 IP 192.168.20.1.60056 > 192.168.20.2.22: Flags [.], ack 341, win 501, options [nop,nop,TS val 2971332474 ecr 164338496], length 0
```
- 解析上面的数据
	- 11:33:48.505721 时间
	- IP 通信协议是IP
	- 192.168.20.1.60056
		- src host 192.168.20.1
		- port 60056
	- > 数据传输方向
	- 192.168.20.2.22
		- dst host 192.168.20.2
		- port 22
	- [P.], seq 36:72 这个数据包带有PUSH的数据传输标志,且传输的数据为整体数据的36-72byte
	- ack 37 ACK的值

## 参考

