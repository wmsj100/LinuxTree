---
title: 数组
date: 2019-04-12 15:40:47	
modify: 
tag: [list]
categories: Shell
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数组

## 概述
- shell的数组和其他编程语言类似
- 数组通过`圆括号`定义，值之间通过`空格`分隔
- `a[0]=1` 也可以直接通过下标的方式定义数组
- 如果直接echo一个数组，只打印数组的第一个值
- `echo ${a[@]}` / `echo ${a[*]}` 读取数组所有值
- `echo ${#a[@]}` / `echo ${#a[*]}` 获取数组的长度
- `echo ${#a[5]}` 获取数组第5个值的长度

## 参考
- [数组](http://c.biancheng.net/cpp/view/7002.html)
