---
title: glibc
date: 2020-06-29 09:45:39
modify: 
tags: [Notes]
categories: Alpine
author: wmsj100
email: wmsj100@hotmail.com
---

# glibc

## 概要

- alpine的glibc环境配置

## 安装

- `sed -i "s@http://dl-cdn.alpinelinux.org/@https://mirrors.huaweicloud.com/@g" /etc/apk/repositories` 替换源
- `https://raw.githubusercontent.com/athalonis/docker-alpine-rpi-glibc-builder/master/glibc-2.26-r1.apk`
- `curl -O https://raw.githubusercontent.com/athalonis/docker-alpine-rpi-glibc-builder/master/glibc-bin-2.26-r1.apk`
- `apk add --allow-untrusted *.apk`

## 参考

