---
title: mktemp
date: 2020-03-23 20:37:41
modify: 2020-04-26 16:00:59  
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# mktemp

## 概要

- 默认创建临时文件在`/tmp`
- 当需要临时在一个文件或者目录内部存储文件或内容时候可以使用这个命令来解除可能的命名冲突问题

## 使用

- `mktemp` `/tmp/tmp.4BVheIfjk5` 创建临时随即名称文件
- `mktemp -d` `/tmp/tmp.St5DNyI9gE/` 创建临时目录
- `mktemp -u` 不创建任何目录或文件，只是打印目录名称

## 参考

