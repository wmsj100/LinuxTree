---
title: yum_cache
date: 2020-05-08 14:49:27
modify: 
tags: [Notes]
categories: CentOS
author: wmsj100
email: wmsj100@hotmail.com
---

# yum_cache

## 概要

- yum的缓存机制默认是关闭的，就是通过yum下载的文件在安装完成后会自动删除，为了保证多个虚拟机安装的软件版本一致，可以利用缓存

## 开启缓存

- `vi /etc/yum.conf`修改`keepcache=1`这样就开启了缓存
- `cachedir`标识了缓存文件的位置
- 这样开启了缓存就可以去缓存目录找到下载的rpm包进行离线安装

## 参考

- [yum cache](https://blog.csdn.net/ljl890705/article/details/78523367)
