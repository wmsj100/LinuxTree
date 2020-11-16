---
title: version_compare
date: 2020-11-16 10:28:50
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# version_compare

## 概要

- 怎么比较python的版本，可以使用`sys.version_info`

## 使用

- `sys.version_info`
	- `sys.version_info(major=3, minor=8, micro=5, releaselevel='final', serial=0)`
- `if sys.version_info >=(3,7)` 判断当前版本是否大于3.7版本
	
## 参考

- [python 官方文档 sys.platform]()
