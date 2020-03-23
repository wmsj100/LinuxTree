---
title: mktemp
date: 2020-03-23 20:37:41
modify: 
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

## 参考

