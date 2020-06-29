---
title: ldconfig
date: 2020-06-29 09:04:59
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# ldconfig

## 概要

- ldconfig命令的主要用途是在/lib和/usr/lib以及动态库配置文件/etc/ld.so.conf内所列出的目录下，搜索出可共享的动态链接库。进而创建出动态装入程序(ld.so)所需的连接和缓存文件。
- 缓存文件默认为/etc/ld.so.cache,此文件保存缓存的已经排序的动态链接库的名称列表。
- 为了让动态链接库为系统所共享，需运行动态链接库的管理命令ldconfig.
- ldconfig通常在系统启动时候运行，当用户安装了一个新的动态链接库时，就需要手动运行这个命令

## 参考

- [ldconfig](https://man.linuxde.net/ldconfig)
