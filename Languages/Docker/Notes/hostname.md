---
title: hostname
date: 2020-04-13 15:29:13
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# hostname

## 概要

- docker里面如何设置hostname，
- `hostnamectl set-hostname ambaria`
- `Could not set property: Failed to set static hostname: Device or resource busy` 提示报错

## 解决

- docker容器的hostname设置无法直接按照上面设置，需要追加参数
- `docker container run -itd --name test1 --hostname ambaria --privileged centos7-base:v0.4 /usr/sbin/init` 这样容器就设置了hostname
- `docker container run -itd --name ambaria01 -p 8080:80 --hostname ambaria01 --add-host ambaria02:172.17.0.5 --add-host ambaria03:172.17.0.7 --privileged ambaria01:v1 /usr/sbin/init` 这样在启动容器时候会指定hostname并且设置hosts，
	- 如果是手动在/etc/hosts文件写死，这样容器重启后就丢失了，但是上面这样在容器启动时候就指定可以避免这样的问题

## 参考

- [docker hostname](https://stackmirror.com/questions/28327458)
