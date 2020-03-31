---
title: cp
date: 2020-03-31 09:37:29
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# cp

## 概要

- 实现了系统主机和docker之间的文件拷贝
- 其实和cp命令类似，就可以理解为一个文件系统到docker文件系统的文件拷贝动作。

## 使用

- `docker cp test1:/tmp/wget-log /tmp` 拷贝docker的文件到系统
- `docker cp /tmp/wget-log test1:/tmp` 拷贝主机文件到docker
- `docker cp -a ./Notes test1:/tmp` 拷贝本地目录到docker

## 参考

