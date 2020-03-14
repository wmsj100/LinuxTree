---
title: ip_route
date: 2020-03-09 11:31:55
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# ip_route

## 概要

- 查看路由信息

## 常用操作

- `ip route show` 查看当前的路由配置情况
- `ip route get 10.10.10.1` 查看ip地址的路由包从那里来
- `ip route add 10.10.10.0/24 via 10.10.10.1` 添加10.10.10.0/24网段路由从10.10.10.1接入
- `ip route append 10.10.10.0/24 via 192.168.0.102` 追加路由,为了平滑切换网络
- `ip route flush 10.10.10.0/24` 清理所有10.10.10.0/24相关的所有路由
- `ip route add default via 192.168.0.103` 添加默认路由
- `ip route change 10.10.10.0/24 via 10.10.10.1` 修改路由
- `ip route add 172.16.5.0/24 via 10.0.0.101 dev eth0` 给网络`172.16.5.0/24`添加`10.0.0.101`的网关

## 参考

- [ip route](https://baijiahao.baidu.com/s?id=1618978745521215381&wfr=spider&for=pc)
- [ip route add for network](https://my.esecuredata.com/index.php?/knowledgebase/article/2/add-a-static-route-on-centos)
