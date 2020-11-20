---
title: linecache
date: 2020-11-20 11:18:06
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# linecache

## 概要

- `linecache`用于从一个文件中读取某行内容
- 读取过程中会使用缓存进行内部优化，
- 即便读取的行数超过文件总行数，也不会报错。

## 使用

- `linecache.getline('build.py', 23)` 读取文件的23行
- `linecache.clearcache()`
- `linecache.lazycache()`

## 参考

