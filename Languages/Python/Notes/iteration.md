---
title: 迭代
date: 2020-01-11 17:45:15
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 迭代

## 概要

- python中有一些很好用的迭代函数

## 迭代分类

- 并行迭代: 同时迭代俩个序列
	- `for key,val in zip(a,c): print(key, val)` 把序列a/c压缩到一块称为元组，然后迭代元组，在for循环中进行解包
- 按索引迭代
	- python正常迭代序列时候是无法获取到当前索引值的，所以如果要修改特定索引值时候就比较麻烦了，
	- enumerate 内建函数，提供索引的地方迭代索引-值对。
	- `for index, val in enumerate(list): print(index, val)`
- 翻转迭代(reversed)
	- 返回的是一个反向迭代器
	- ''.join(reversed(a))
	- next(reversed(a))
- 排序迭代(sorted): 直接返回一个排序后的list

## 创建迭代器

- iter: 可以创建一个迭代器
- next(iter): 可以读取下一个迭代器的值，最后以StopIteration结束
- 迭代器只能读取一次，也就是说迭代器只能list化一次，第二次list(iter),返回一个空数组

## 参考


