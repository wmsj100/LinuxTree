---
title: export
date: 2020-07-07 20:49:18
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# export

## 概要

- export可以将一个正在运行的容器到处到文件中,
- 可以通过commit将容器提交为镜像,然后通过save来导出镜像.
- export只是导出当前容器的一个快照,容器的所有元信息和历史提交记录都会丢失.

## 命令

- `docker container export -o test.tar test1` 将容器test1导出到文件test.tar文件中

## 参考

