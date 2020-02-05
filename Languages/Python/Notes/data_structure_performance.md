---
title: 数据结构的性能
date: 2020-02-05 15:21:59
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 数据结构的性能

## 概要

- 字典和集合都是经过高度优化过的数据结构。
- 对于大的数据量，优先使用集合替换列表。
- 越是大的数据量，字典和集合的优势越明显。

## 原理

- 字典和集合能如此高校，和它们内部的数据结构密不可分。
- 不同于其他数据结构，字典和集合的内部结构都是一张哈希表
	- 对于字典而言:这张表存储了哈希值、键和值3个元素
	- 对于集合，哈希表内只存储单一元素。
- 对于哈希值的操作可以提升曾删改查效率

## 范例

- 集合对比list的性能优势
```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020  <@DEEP-2020TGTVHB>
#
# Distributed under terms of the MIT license.

"""
比较列表和集合的性能
"""
import time

def find_union_price_useing_list(products):
    unique_price_list = []

    for __, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)

    return len(unique_price_list)

def find_unique_price_useing_set(products):
    unique_price_set = set()

    for __, price in products:
        if price not in unique_price_set:
            unique_price_set.add(price)

    return len(unique_price_set)

id = [ x for x in range(100000)]
price = [x for x in range(200000,300000)]
products = list(zip(id, price))

# time for list
start_time_list = time.perf_counter()
find_union_price_useing_list(products)
end_time_list = time.perf_counter()
print("time is {}".format(end_time_list - start_time_list))
# time is 106.41455579999999

start_time_set = time.perf_counter()
find_unique_price_useing_set(products)
end_time_set = time.perf_counter()
print("time is {}".format(end_time_set - start_time_set))
# 0.030215960000006703

# 可以看到俩者差距有3521倍
```

## 参考

- [python dict/set 性能解析](http://c.biancheng.net/view/vip_6003.html)
