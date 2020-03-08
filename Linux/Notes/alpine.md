---
title: alpine
date: 2020-03-08 17:42:20
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# alpine

## 概要

- 这是docker官方的linux发行版本,体积很小,面向安全的轻量级系统
- `cat /etc/os-version` 查看系统发行版本`

## 配置源

- ` /etc/apk/repositories`
- `sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories`

## 常用命令

- `apk update`
- `apk search`
- `apk add openssh openntp vim`
- `apk info` 列出已安装的软件包
- `apk upgrade` 升级所有软件
- `apk add --upgrade busybox` 指定升级部分软件包
- `apk del openssh`

## Linux服务管理

- alpine没有使用fedora的systemctl来管理服务,使用RC系列命令
- `apk add openrc`
- `openrc` 启动服务管理
- `rc-update show` 展示当前的所有runlevel
- `rc-update add nginx` 添加一个服务

## 参考

- [alpine 系统使用](https://www.cnblogs.com/jackadam/p/9290366.html)
