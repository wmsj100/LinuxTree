---
title: readlink
date: 2020-07-01 15:16:26
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# readlink

## 概要

- `readlink`是linux系统中常用的一个工具，主要用来找出符号链接指向的位置

## 使用

- `readlink /usr/bin/java` `/etc/alternatives/java`
- `readlink -f /usr/bin/java` `/usr/lib/jvm/java-11-openjdk-11.0.7.10-4.el7_8.aarch64/bin/java` 递归查找出文件位置

## 参考

- [readlink](https://blog.csdn.net/diabloneo/article/details/7173438)
