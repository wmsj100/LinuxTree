---
title: lib
date: 2020-04-08 11:40:12
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# lib

## 概要

- lib目录是动态库的存储目录
- centos还会有一个`/lib64`目录，当前64架构的动态库都会存储到`/lib64`
- 不同发行版的库文件目录结构不同
- centos7的`/lib ==> /usr/lib /lib64 ==> /usr/lib64`,这个和其他发行版都不同
- 其他发行版，比如ubuntu/archlinux/alpine等/lib|/lib64和/usr/lib|/usr/lib64是分开的，不同的。

## 参考

