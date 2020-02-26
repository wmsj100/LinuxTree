---
title: awk
date: 2020-02-26 20:34:55
modify: 
tags: [Note]
categories: Shell
author: wmsj100
email: wmsj100@hotmail.com
---

# awk

## 概要

- 排版工具

## 常用命令

- `grep -nrw 'blog' . | awk -F ':' '{print $1}'` 找出所有包含blog的文件，并且按照分隔符':'打印第一列。
- `grep -nrw 'blog' . | awk -F ':' '{print $1} | sort | uniq`
- `sed -i 's/blog/yiqin/g'  `grep -rw 'blog' | awk -F ':' '{print $1}' | sort | uniq`` 去重并且用sed进行替换

## 参考

