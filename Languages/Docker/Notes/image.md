---
title: image
date: 2020-03-03 09:35:49
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# image

## 概要

- 关于镜像的操作

## 基础概念

- 镜像由一些松耦合的只读镜像层组成。
- docker负责堆叠这些镜像层，并且将它们表示为单个统一的对象。
- `docker image inspect ubuntu:latest` 查看Ubuntu的镜像分层情况。
- 多个镜像分层可以实现共享

## 镜像散列值

- 每一个镜像都有一个基于内容的密码散列值，这个散列值保证镜像文件完整并且没有被修改
- 如果修改内容，这个散列值就无法匹配。
- 这个散列值会随着`docker image pull`同时返回
- `docker image ls --digests ubuntu` 查看ubuntu的散列值
- `docker image pull alpine@sha256:ab00606a42621fb68f2ed6ad3c88be54397f981a7b70a79db3d1172b11c4367d` 可以通过散列值来拉去镜像，这样的镜像没有标签，None，

## 常用命令

- `docker image ls` 查看当前镜像
- `docker image ls -a` 包括停止的镜像
- `docker image build -t test:latest .` 在当前目录创建镜像，必须在Dockfile文件所在目录
- `docker image rm jenkins:latest` 删除镜像，会彻底删除镜像文件
- docker的本地镜像位于`/var/lib/docker`
- `docker image pull ubuntu:latest` 拉取最新镜像
- `docker image prune` 移除所有没有标签的镜像
- `docker image ls --filter before='ubuntu'` 在之前被创建的全部镜像
- `docker image ls --filter=reference="*:latest"` 返回标签为latest的所有镜像
- `docker search nginx` 搜索docker镜像仓库，会显示所有官方或非官方的镜像
- `docker image ls -q` 只返回镜像的imageID
- `docker image rm $(docker image ls -q) -f` 可以通过这个命令来删除全部本地的镜像文件

## 参考

