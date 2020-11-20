---
title: free
date: 2020-11-20 16:19:41
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# free

## 概要

- 该命令用于查看当前系统的内存使用情况

## 使用

- `free -h` 查看当前系统的内存使用情况
- `echo 1 > /proc/sys/vm/drop_caches` clear page cache
- `echo 2 > /proc/sys/vm/drop_caches` clear dentries and inodes
- `echo 3 > /proc/sys/vm/drop_caches` clear page cache,dentries,inodes

## 参考

- [linux mem clear](https://www.tecmint.com/clear-ram-memory-cache-buffer-and-swap-space-on-linux/)
