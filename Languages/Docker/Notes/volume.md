---
title: volume
date: 2020-03-05 22:25:05
modify: 2020-06-02 11:02:38 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# volume

## 概要

- 卷存储，是docker的持久存储，可以和容器挂载，且支持不同驱动
- 数据卷是可以在多个容器中共享的，如此来实现容器数据共享，就是说一个数据卷可以在多个容器创建时候进行mount挂载

## 命令

- `docker volume create myvol` 创建卷
- `docker volume prune` 删除全部未装入容器的所有卷
- `docker volune rm myvlo` 删除指定卷，如果该卷正在被使用，无法删除
- `docker container run -it --name vol1 --mount source=myvle,target=/code alpine`
	- 创建容器并且同时挂载卷myval
	- 如果myval没有创建就先创建
	- 把卷挂载到容器的/code目录
- `/var/lib/docker/volumes/myvol/_data/hello.md` 删除容器，然后查看卷仍然存在，查看卷下的文件也存在，数据也存在
- `docker service create --name test2 --network uber-net --mount source=myvol,target=/code alpine sleep 1d`
	- 卷也可以挂载到集群中，
	- 上面的集群只创建了一个节点
	- 添加到网络uber-net,挂载卷myvol到/code
- docker的卷也可以在集群中共享，公共的外部存储通过第三方驱动来集成进来，需要关注数据损坏

## 参考

- [docker数据卷](https://www.cnblogs.com/sparkdev/p/8504050.html)
