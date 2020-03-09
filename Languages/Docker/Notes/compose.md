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
- 知道了是一个python插件还是想着如何下载这个二进制文件,
- `pip install docker-compose` 就可以下载
- 是一个用户定义和运行多个容器的Docker应用程序,通过YMAL文件来配置应用服务.
- 是Docker官方开源项目,负责对Docker容器集群的快速编排.

## 简介

- `Docker-compose`将所管理的容器分为三层,分别是工程(project)/服务(service)/容器(container)
- `Docker-compose`运行目录下所有的文件(docker-compose.yml,extends文件或者环境变量文件)组成一个工程,若无特殊指定工程名即为当前目录名.
- 一个工程当中可以包含多个服务,每个服务中定义了容器运行的镜像,参数,依赖.
- 一个服务当中可包括多个容器实例
- `Docker-compose`工程配置文件默认为`docker-compose.yml`,可以通过环境变量`COMPOSE_FILE`或`-f`参数自定义配置文件,其定义了多个有依赖关系的服务及每个服务运行的容器.
- 

## 使用

- 在Dockfile中定义应用环境,使其可以在任何地方复制
- 在docker-compose.yml中定义组成应用程序的服务,以便他们可以在隔离环境中一起运行
- 最后运行`docker-compose up/down`来启动应用程序.

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

- [docker-compose 详解](https://www.cnblogs.com/minseo/p/11548177.html)
