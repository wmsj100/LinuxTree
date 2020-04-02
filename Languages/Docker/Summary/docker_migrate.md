---
title: docker迁移磁盘
date: 2020-04-02 16:52:17
modify: 
tags: [Summary]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# docker迁移磁盘

## 概要

- docker刚开始默认是在`/var/lib/docker`这样占用的是系统盘
- 现在增加来数据盘，重新把之前的所有docker迁移到数据盘

## 操作

- `mount /dev/vdc /docker` 挂载数据盘
- `rsync -a /var/lib/docker /docker` 完全拷贝docker的所有内容到目标
- `docker container stop all containers` 停止所有的容器
- `systemctl stop docker.service` 停止docker服务
- `rm -rf /var/lib/docker` 删除旧的docker数据
- `ln -s /docker  /var/lib/docker` 在原有位置创建软链接
- `systemctl start docker.service` 启动docker服务
- `docker container start all container` 启动所有容器
- `docker container exec -it centos_wmsj bash` 登录一个容器验证可用性，至此迁移完成

## 参考

