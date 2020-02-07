---
title: 推导式
date: 2020-02-07 08:04:55
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 推导式

## 概要

- 推导式是python独有的一种特性。
- 使用推导式可以快速生成列表、元组、字典以及集合类型的数据

## 列表推导式

- 最常见的就是列表推导式，可以利用range区间、元组、列表、字典、集合等数据类型快速生成一个满足指定需求的列表。
- `[ x for x in range(10) if x%2 == 0]`

## 元组推导式

- 和列表推导式基本类似，
- 元组推导式返回的是一个生成器，需要使用tuple/for/__next__()来读取生成器的值
- `(x for x in range(10))` `<generator object <genexpr> at 0x7f52c84edf68>`
- 对生成器读取后，原生成器对象将不复存在，再次读取只有一个空元组

## 字典推导式

- 和列表推导式类似
- `{key:len(key) for key in ['name', 'age']}` `{'name': 4, 'age': 3, 'address': 7}`
- `{val:key for key,val in olddict}` 可以交互字典的键值对

## 集合推导式

- 和字典推导式类似
- `{x for x in range(10)}` `{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}`
- `{x for x in [1,2,1,2,3]}` `{1, 2, 3}`
- 集合推导式中没有重复的元素

## 参考

- [python 推导式](http://c.biancheng.net/view/vip_6008.html)
