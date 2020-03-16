---
title: nmap
date: 2020-03-16 14:14:10
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# nmap

## 概要

- nmap: 是一个很强悍的软件,可以进行端口扫描和主机发现
- 直接可以使用这个命令扫描一个已知ip的主机上面开启的服务,可以详细列出服务的版本号,系统等信息
- nmap是可以做间谍软件的工具

## 参数介绍

- -v 详细进程
- sS tcp syn
- sT Tcp扫描
- sA ack 扫描
- sU udp扫描
- F 快速扫描,常用默认100个端口
- T4 快速扫描,网络的连通性和性能

## 常用命令

- `nmap -sP 192.168.0.0/24` 在当前主机扫描发现`192.168.0.0/24`网段的主机
- `nmap -T4 -Pn 192.168.20.2` 扫描目标主机的端口
- `nmap -sn 192.168.0.0/24` 不扫描端口,直接扫描主机是否开机
- `nmap -p 80,20 192.168.20.2`
- `nmap -p 1-100 192.168.20.2` 端口测试
- `nmap -sV 192.168.0.1` 服务版本测试
- `nmap -O 192.168.20.2` 扫描os
- `nmap 192.168.0.1` 扫描单个目标
- `nmap 192.168.0.1 192.168.0.2` 扫描多个网络
- `nmap 192.168.20.1-100` 扫描连续ip

- 主机存活状态扫描
	- `nmap -Pn 192.168.20.2` 
	- `nmap -sn ip`
	- `nmap -sT ip` 使用TCP扫描
	- `nmap -sS ip` 使用SYN扫描
	- `nmap -sA ip` 使用ACK扫描
	- `nmap -sU ip` 使用UDP扫描
	- `nmap -sP ip` 使用ping扫描
	- `nmap -PO ip` 
- 端口扫描
	- `nmap 23 ip`
	- `nmap 23,80 ip` 
	- `nmap -F ip` 随机100个

## 范例

```
pi@raspPI:~ $ nmap -A -T4 -Pn 111.229.241.222
Starting Nmap 7.70 ( https://nmap.org ) at 2020-03-16 14:24 CST
Nmap scan report for 111.229.241.222
Host is up (0.035s latency).
Not shown: 998 filtered ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e9:3e:3a:ac:a1:e6:15:32:60:2f:be:a4:56:72:38:0e (RSA)
|   256 a2:e1:b7:d1:a1:b5:bb:bc:a7:2d:60:30:c0:3c:c1:77 (ECDSA)
|_  256 d6:3f:73:2d:70:48:e8:20:c7:0d:9a:3f:f0:d3:73:4e (ED25519)
3306/tcp open  mysql   MySQL 5.7.29-0ubuntu0.18.04.1
| mysql-info:
|   Protocol: 10
|   Version: 5.7.29-0ubuntu0.18.04.1
|   Thread ID: 753
|   Capabilities flags: 65535
|   Some Capabilities: Speaks41ProtocolNew, ODBCClient, Support41Auth, SwitchToSSLAfterHandshake, Speaks41ProtocolOld, SupportsLoadDataLocal, ConnectWithDatabase, DontAllowDatabaseTableColumn, LongColumnFlag, IgnoreSigpipes, SupportsCompression, IgnoreSpaceBeforeParenthesis, FoundRows, LongPassword, InteractiveClient, SupportsTransactions, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: 5cL7\x0EpgG#)\x0FQ\x08\x02Z\x03Nlu8
|_  Auth Plugin Name: 96
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.42 seconds
```
## 参考

- [nmap 使用](https://www.cnblogs.com/biaochen/p/11307589.html)
