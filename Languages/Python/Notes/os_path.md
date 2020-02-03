---
title: os_path
date: 2020-02-03 18:35:27
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# os_path

## 概要

- 介绍os模块的path模块

## 常用方法

> 判断操作是在path模块

- `os.path.exists(path)` 判断文件或目录是否存在
- `os.path.isfile(path)` 判断是否为文件
- `os.path.isdir(path)` 判断是否为目录
- `os.path.basename(path)` 返回文件名
- `os.path.dirname(path)` 返回目录名
- `os.path.getsize(name)` 获取文件的size，字节单位
- `os.path.abspath(name)` 获取绝对路径
- `os.path.join(path, name)` 连接目录或文件，按照目录分隔符
- `os.path.realpath(__file__)` 获取文件所在的绝对路径

## 参考
