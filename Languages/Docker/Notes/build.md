---
title: build
date: 2020-06-24 17:43:06
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# build

## 概要

- build用来构建镜像，
- 通常一个Dockerfile只有一个FROM，但是从docker17.05版本之后支持了多阶段镜像构建
- 这绝对是一个伟大的功能，这样可以把编译和构建分离开，把编译生成的文件拷贝到运行环境即可，这样可以大大缩小镜像的尺寸。
- 多个FROM中只有最后一个是生效的。

## 参考

- [docker from](https://tonybai.com/2017/11/11/multi-stage-image-build-in-docker/)
- [docker from](http://dockone.io/article/8179)
