---
title: Dockerfile
date: 2020-03-03 20:02:52
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# Dockerfile

## 概要

- 这个文件是构建docker镜像的命令文件

## 命令

- 新增镜像层的指令:
	- FROM
	- RUN
	- COPY
- 新增元数据的指令:
	- EXPOSE
	- WORKDIR
	- ENV
	- ENTERPOINT
- 如果指令的作用是向镜像中添加新的文件或者程序，那么这条指令就会新建镜像层
- 如果只是告诉dockers如何完成构建或者如何运行应用程序，那么就只会增加镜像的元数据。

## 参考

