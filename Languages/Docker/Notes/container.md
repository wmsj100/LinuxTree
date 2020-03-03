---
title: container
date: 2020-03-03 09:03:31
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# container

## 概要

- 容器的基础命令

## 命令

- `docker container ls` 查看正在运行的容器
- `docker container exec -it 6ee3d518b856 bash` 可以通过containerID来连接到容器环境。
- `docker container stop 6ee3d518b856` 停止容器
- `docker container start 6ee3d518b856` 启动容器
- `docker container ls -a` 默认只列出运行中的容器，通过这个命令可以列出所有容器
- `docker container rm 6ee3d518b856` 删除指定容器
	- 删除容器之前需要先stop容器
	- 删除镜像image之前需要先删除容器

## 参考

