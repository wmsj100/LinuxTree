---
title: reduce
date: 2020-02-07 21:55:55
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# reduce

## 概要

- 也是一个函数式编程的方法
- 通常用来对一个集合做一些累积操作
- `reduce(function, iterable)`
- function规定必须是一个包含2个参数的函数；
- 该方法以及放置再`functools`
- reduce直接返回一个值

## 范例

- 对list进行累加
```python
import functools
a = [1, 2, 3, 4, 5]
functools.reduce(lambda x,y:x+y, a) # 15
```

## 参考

- [python reduce](http://c.biancheng.net/view/vip_6064.html)
