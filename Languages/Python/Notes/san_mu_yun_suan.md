---
title: 三目运算
date: 2020-02-04 19:50:04
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 三目运算

## 概要

- 编程语言基本都具备的复杂运算

## 介绍

- python是一种极简主义的编程语言，它没有引入`?:`这个新的运算符，而是使用已有的`if else`关键字来实现相同功能
- `exp1 if contion else exp2`
- `max = a if a>b else b` 如果`a>b`，`max=a`，否则`max=b`
- 三目运算也可以嵌套，是右运算，从右往左
- `a if a>b else c if c>a else a` == `a if a>b else (c if c>a else a)`

## 参考

- [python 三目运算](http://c.biancheng.net/view/2187.html)
