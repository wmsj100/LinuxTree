---
title: arp
date: 2020-03-14 13:17:38
modify: 
tags: [Notes]
categories: Network
author: wmsj100
email: wmsj100@hotmail.com
---

# arp

## 概要

- arp: address resolution protocol 网络地址协议
- ip和mac地址的对应关系通过arp来管理
- 当想要了解某个ip配置于那张网卡上时,我们的主机会对整个局域网发送出ARP数据包,对方接受到ARP数据包后就会返回它的MAC
- 这样主机就知道ip和mac的对应关系了
- 获取到的ARP会写入ARP table,内存数据中,记录20分钟.
- 随着网络计算机的IP变动而变动

## 使用

- `ip neigh show`
```
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/Notes$ ip neigh show 
192.168.0.1 dev wlx081079db1327 lladdr b0:95:8e:c4:ae:1d REACHABLE
192.168.0.101 dev wlx081079db1327  INCOMPLETE
192.168.0.102 dev wlx081079db1327 lladdr b8:27:eb:4d:dd:05 STALE
192.168.0.100 dev wlx081079db1327 lladdr d8:63:75:b3:8c:a3 STALE
```

## 参考

