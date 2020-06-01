---
title: 数据卷的价值
date: 2020-06-01 15:06:52
modify: 
tags: [Summary]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# 数据卷的价值

## 概要

- 因为系统被重装导致所有数据找补回来，或者说我看到哪个体系结构后发现很难找回来。
- 然后就意识到一点，为什么当初就不创建一个数据卷出来，反正那些数据是有用的，而且可能要在当前操作系统进行验证，为什么不通过数据卷的技术直接和操作系统共享文件。
- 而且这样还省去了容器直接数据共享的问题，
- 这也算是一个教训，就是无论容器是打算来做什么的，一定要先创建数据卷并且挂载到当前容器上面。

## 使用

- `docker volume create spark`
- `docker container run -itd --name spark --hostname Kunpeng --privileged --mount source=spark,target=/data centos:7 /usr/sbin/init` 这样就把创建的数据卷挂载到了容器上面。

## 参考

