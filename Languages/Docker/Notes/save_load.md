---
title: 镜像导入导出
date: 2020-03-05 09:43:20
modify: 
tags: [Notes]
categories: Docker
author: wmsj100
email: wmsj100@hotmail.com
---

# 镜像导入导出

## 概要

- 制作的镜像不一定要上传到docker hub才可以分享，也可以导入和导出为tar包进行分享

## save

- `docker save -o /home/wmsj100/web_rasp.tar web_rasp:latest` 导出镜像到本地

## load

- `docker load --input web_rasp.tar` 导入镜像tar包

## 参考

- [docker load/save](https://blog.csdn.net/u011365831/article/details/81430513)
