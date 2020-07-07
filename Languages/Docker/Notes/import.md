---
title: import
date: 2020-07-07 20:58:07
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# import

## 概要

- import用于导入通过export导出的容器镜像,
- 导出的容器镜像必须先导入为镜像文件,然后通过启动为容器

## 使用

- `docker import test1.tar test1/alpine:1` 把导出的容器导入到镜像中

## 参考

