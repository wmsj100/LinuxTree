---
title: id
date: 2020-11-26 16:30:15
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# id

## 概要

- id命令可以展示用户的uid和gid
- root用户的`uid/gid`都是0，所以可以通过id值是否为0来判断当前执行用户是否为root

## 使用

- `id`
- `id -u`
- `id -g`
- `id -G` 展示用户所有附属的group id

## 参考

- [id man](https://man.linuxde.net/id)
