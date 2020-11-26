---
title: mountpoint
date: 2020-11-26 17:04:50
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# mountpoint

## 概要

- 判断指定的目录是否是加载点,如果是挂载点就返回0，否则返回非0
- 所谓的挂载点是指当前目录或父目录是通过mount挂载的文件系统

## 使用

- `mountpoint -q /mnt` 静默判断`/mnt`是否是加载点

## 参考

- [mountpoint](https://man.linuxde.net/mountpoint)
