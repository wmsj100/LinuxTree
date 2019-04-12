---
title: shell运算
date: 2019-04-12 14:38:49	
modify: 
tag: [expr]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 运算

## 概述
- shell的四则运算通过`expr`来实现
- 运算符前后必须添加空格
- `*` 必须进行转义

## 范例
- a=`expr 1 + 2`
- a=`expr 1 - 2`
- a=$(expr 1 \* 2)
- a=$(expr 1 / 2)
- a=$(expr 1 % 2)

## 参考
- [expr运算](http://c.biancheng.net/cpp/view/2736.html)
