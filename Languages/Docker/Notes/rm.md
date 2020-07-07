---
title: rm
date: 2020-07-07 20:32:42
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# rm

## 概要

- `docker container rm xxx` 删除一个停止的容器
- `docker container rm -f xx` 强制删除一个运行中的容器	
	- Docker会先发送GIGKILL信号给容器,终止其中的应用,之后强行删除

## 参考

