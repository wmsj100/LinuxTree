---
title: init.d
date: 2020-11-26 16:21:19
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# init.d

## 概要

- init.d目录的文件是linux执行的第一个进程
- 系统启动过程中需要自动拉起的文件或者说需要通过service来管理的服务需要在该目录创建脚本
- 通常服务需要支持的命令有`start/stop/restart/force-stop/reload/status`
- 该服务或者说该启动流程在`centos7`中已经被`systemctl`取代了，因为init启动脚本是按顺序执行的，没办法并发执行俩个不相关的服务
- 但在当前系统中`init`脚本还是得到了保留

## 术语

- `log_failure_msg` 打印error日志


## 参考

