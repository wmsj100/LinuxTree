---
title: compose
date: 2020-03-03 21:45:25
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# compose

## 概要

- `docker-compose`是docker的一个python插件，被docker公司收购并且用于管理多容器

## 使用

- `docker-compose`默认读取项目的`docker-compose.yml`文件
- 通过`compose`文件定义的多容器应用被称为'compose应用'
- `docker-compose up`启动一个'compose应用'
- `docker-compose up -d` 将应用放到后台执行。
- `docker-compose -f prod-que.yml -d` 指定配置文件并且放到后台执行
- `docker-compose down` 该命令需要在`docker-compose.yml`目录执行，停止'compose应用'，应用被删除，仅留下了卷和镜像，网络也被删除
- `docker-compose ps` 查看当前compose应用的状态
- `docker-compose stop` 停止应用
- `docker-componse rm` 用于删除已经停止的应用
- `docker-compose restart` 重启应用
- `docker volume ls`
- `docker network ls`
- 保存在卷中的文件会持久存在，直接修改卷中的文件会立刻从容器的应用中反馈出来。
- `docker volume inspect counter-app_counter-vol | grep Mount` 查看docker的卷的挂载路径
	- `"Mountpoint": "/var/lib/docker/volumes/counter-app_counter-vol/_data",`

## 参考

