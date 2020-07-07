---
title: run
date: 2020-07-07 20:00:26
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# run

## 概要

- run会先创建一个容器,在使用start启动容器

## 命令

- `docker run -it --name test1 --rm ubuntu bash` 启动一个容器并进入交互界面,等容器退出后会直接删除容器

## 流程

- `docker run ubuntu /bin/bash 'hello world'`
- 检查本地是否存在指定镜像,不存在就从公有仓库下载
- 利用镜像创建一个容器,并启动该容器
- 分配一个文件系统给容器,并在只读的镜像层外面挂载一层可读写层
- 从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
- 从网桥的地址池中配置一个IP地址给容器
- 执行用户指定的应用程序
- 执行完毕后容器被自动终止

## 参考

