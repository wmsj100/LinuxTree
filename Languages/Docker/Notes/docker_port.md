---
title: docker_port
date: 2020-03-07 12:04:35
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# docker_port

## 概要

- docker服务常用端口

## 详情

- docker常用的端口如下
	- 2377/tcp 彼此swarm节点通信端口
	- 7946/tcp
	- 7946/udp 
- ubuntu默认的防火墙策略是阻止所有进入的端口,所以需要手动放开这些端口的监听
- `sudo ufw allow 2377/tcp`
- `sudo ufw allow 7946/tcp`
- `sudo ufw allow 7946/udp`
- `docker node ls` 就可以看到节点是正常状态

## 参考

