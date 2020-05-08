---
title: docker_Root
date: 2020-05-08 20:23:45
modify: 
tags: [Summary]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# docker_Root

## 概要

- docker默认的数据路径地址是`/var/lib/docker`，如何修改这个路径

## 方法

- `vi /etc/docker/daemon.json`添加配置`{"graph": "/data/docker"}`
- `rsync -a /var/lib/docker/ /docker` 拷贝所有文件到/docker, 
- `rm -rf /var/lib/docker`
- 此时就俩个方法，
	- `ln -s /docker /var/lib/docker` 软链接的方式
	- `mkdir /var/lib/docker; mount /dev/vdb1 /var/lib/docker` 直接挂载磁盘到这个目录

## 参考

