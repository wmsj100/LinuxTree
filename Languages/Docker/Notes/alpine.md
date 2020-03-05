---
title: alpine
date: 2020-03-05 14:55:24
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# alpine

## 概要

- 这个镜像是由dockers官方制作的基于alpine的镜像
- 之前使用基层镜像用的是ubuntu，由50M左右，这个镜像只有不到5M

## 容器

- `docker container run -d --name c1 --network localnet alpine sleep 1d` 
- 这样就可以基于那个镜像制作一个容器。
- `docker container run -it --name c2 --network localnet alpine sh` 接入alpine容器
- 这个linux中基础命令是齐全的，该有的都有。连dos2unix都由

## 参考

