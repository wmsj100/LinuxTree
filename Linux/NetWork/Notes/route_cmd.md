---
title: route_cmd
date: 2020-03-09 10:58:18
modify: 
tags: [Notes]
categories: NetWork
author: wmsj100
email: wmsj100@hotmail.com
---

# route_cmd

## 概要

- 添加路由信息

## 常用命令

- `route` 查看路由信息,会重新查询生成表,速度很慢,
- `route -n`直接返回当前信息,不重新查询
- `route add default gw 192.168.0.1 dev eth0` 添加默认路由给eth0
- `route del -net 192.168.1.0 netmask 255.255.255.0 dev eth0` 删除eth0的路由
- `route del default gw 192.168.0.1 dev eth0`

## 参考

