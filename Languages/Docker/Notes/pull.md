---
title: pull
date: 2020-06-23 15:08:24
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# pull

## 概要

- docker拉取镜像的操作
- 默认拉取镜像时候按照当前平台自动下载，但是可以通过开启“experimental”开关来指定不同平台的镜像

## 开启

- `vi /etc/docker/daemon.json` `"experimental": true`
- `systemctl restart docker.service` 重启docker服务
- `docker pull --platform linux/arm64 busybox` 在x86平台下载arm架构

## 参考

- [docker pull experimental](https://stackoverflow.com/questions/44346322/how-to-run-docker-with-experimental-functions-on-ubuntu-16-04)
