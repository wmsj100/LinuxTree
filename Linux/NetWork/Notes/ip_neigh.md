---
title: ip_neigh
date: 2020-03-14 13:39:34
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# ip_neigh

## 概要

- 查看当前局域网的arp Address Resolution Protocol
- 即IP和MAC的对应关系,这个对应关系是通过在局域网内部发送ARP包来收集的
- 这个对应表是保存在内存中的,每隔20分钟自动更新

## 使用

- ip neigh show
ubuntu@Ubuntu:~/Documents/Github/LinuxTree/Linux/NetWork/Notes$ ip neigh
192.168.0.1 dev wlx081079db1327 lladdr b0:95:8e:c4:ae:1d REACHABLE
192.168.0.101 dev wlx081079db1327  INCOMPLETE
192.168.0.102 dev wlx081079db1327 lladdr b8:27:eb:4d:dd:05 STALE
192.168.0.100 dev wlx081079db1327 lladdr d8:63:75:b3:8c:a3 STALE
```

## 参考

