---
title: rename
date: 2020-09-15 17:11:11
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# rename

## 概要

- 批量修改文件名称

## 使用

- `rename s/.cpython36-opt1//`
- `find -name "*.pyc" -exec rename 's/.cpython36-opt1//' {} \;`

## 参考

