---
title: overlay
date: 2020-03-05 21:55:59
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# overlay

## 概要

- 覆盖网络，是docker实现的在不同网段间打通流量的技术
- 覆盖网络是针对机器swarm中的节点进行互相通信的。

## 操作

- `docker netword create -d overlay uber-net` 创建了覆盖网络
- `docker service create -d --name test1 --network uber-net --replicates 2 alpine sleep 1d` 
- 在集群中创建服务test1，部署节点2个，创建在覆盖网络中
- `docker container inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' imageid` 获取容器的IP地址
- `docker container exec -it test1. sh` 登录一个节点，去ping另一个节点，流量是打通的

## 参考

