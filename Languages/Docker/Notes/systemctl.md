---
title: systemctl
date: 2020-04-03 17:29:50
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# systemctl

## 概要

- docker容器默认启动之后是没有办法通过systemctl来管理服务的，这个需要执行下面的命令
- `docker commit -a wmsj100 -m "wanghao container" centos7_wmsj100 centos7_wmsj100:latest` 这样提交一个镜像
- `docker container run -itd --name centos7_wanghao1 --privileged=true centos7_wanghao_images:latest /usr/sbin/init`
- 这样启动之后就可以在容器中通过systemctl来管理服务来。

## 参考

- [docker systemctl](https://blog.csdn.net/m0_37886429/article/details/80350659)
