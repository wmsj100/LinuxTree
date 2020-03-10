---
title: docker占用端口
date: 2020-03-10 20:26:05
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# docker占用端口

## 概要

- docker在运行中会占用一些端口,如果虚拟机有设置防火墙,需要开放这些端口出来.

## 端口

- `2377/tcp`: This port is used for communication between the nodes of Docker Swarm or cluster.
- `2376/tcp`: secure Docker client communication. This port is required for Docker Machine to work.
- `7946/tcp && 7946/udp`: for communication among nodes
- `4789/udp`: for overlay network traffic

## 参考

- [docker port开放](https://blog.csdn.net/xiunai78/article/details/86713380)
