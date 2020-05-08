---
title: seq
date: 2020-05-08 10:52:10
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# seq

## 概要

- 用于生成某个数到另一个数的所有整数

## 使用

- `seq 1 9`
- `seq -w 1 20` 输出的数据同宽，比如01 03
- `seq -f "str%3g" 1 5` 指定每个数据的前缀，并指定每个数据的宽度
- `seq -f "str%03g" 1 5` 用0填充保持数据宽度一致
- `seq -f "str%g" 1 5` str1 str2
- `seq -s " " -f "str%g" 1 5` 输出的数据用空格分隔并且一行输出

## 参考

- [seq用法](https://man.linuxde.net/seq)
