---
title: network
date: 2020-03-05 12:49:06
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# network

## 概要

- docker的网络支持CNM标准(container network model)
- libnetwork是对CNM的实现
- 驱动时网络的数据层，内置bridge/overlay等网络
- docker创建容器时默认创建Bridge(单机桥接网络)，每个docker主机都有一个默认的单机桥接网络。
- 创建容器时如果不指定网络默认都接入该网络
- 默认的`bridge`网络被映射到内核中为`docker0`的linux网桥。

## 常见操作

- `docker network inspect uber-net` 查看当前网络的详情
- 

## 参考

