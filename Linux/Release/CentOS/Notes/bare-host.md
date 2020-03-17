---
title: bare-host
date: 2020-03-17 12:17:01
modify: 
tags: [Notes]
categories: CentOS
author: wmsj100
email: wmsj100@hotmail.com
---

# bare-host

## 概要

- 我刚刚重装完centos之后,然后又装了mariadb/docker,然后用nmap扫描了以下自己的主机,
- centos的selinux默认是不开启的,所以我修改并开启了selinux
- nmap的扫描结果如下
```
wmsj100@UbuntuOS:~/Documents/GitHub/LinuxTree/Linux/Release/CentOS/Notes$ nmap -A 111.229.241.222

Starting Nmap 7.60 ( https://nmap.org ) at 2020-03-17 12:21 CST
Nmap scan report for 111.229.241.222
Host is up (0.035s latency).
Not shown: 988 closed ports
PORT     STATE    SERVICE        VERSION
22/tcp   open     ssh            OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 ab:13:55:3b:39:7b:7c:98:1d:05:ee:74:27:cd:e3:a4 (RSA)
|   256 65:c9:db:64:13:b7:b2:13:68:48:86:95:21:1a:a1:c3 (ECDSA)
|_  256 f7:ce:49:4d:cd:77:a1:7b:6f:cc:b5:41:7f:c8:dc:9d (EdDSA)
135/tcp  filtered msrpc
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
593/tcp  filtered http-rpc-epmap
901/tcp  filtered samba-swat
1025/tcp filtered NFS-or-IIS
3128/tcp filtered squid-http
3306/tcp open     mysql          MariaDB (unauthorized)
4444/tcp filtered krb524
6129/tcp filtered unknown
6667/tcp filtered irc

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.59 seconds
```
- 可以扫描到我的这么多端口,当前的主机,几乎就是裸奔状态,因为可以针对端口发起攻击

## 参考

