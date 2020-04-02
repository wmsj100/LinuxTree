---
title: overlay2
date: 2020-04-02 17:51:47
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# overlay2

## 概要

- overlay2是docker默认的文件系统
- overlay2通常位于`/var/lib/docker/overlay2/`
- overlay2的目录结构如下：`diff/link/lower/merged/work`目录
- 容器的镜像是由多个只读的镜像层叠加组成的，每层的不同在diff目录中呈现，层与层的关系通过link定义，
- 当启动一个容器时候就是在加载的image上层进行读写，当通过commit提交时候，就会把当前层存储为只读层，
- 通过这样的分层可以提高镜像的存储利用率，也可以在传输时候只传输差异层，或者下载时候也只会下载差异层。

## 参考

