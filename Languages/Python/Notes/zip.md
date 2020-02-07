---
title: zip
date: 2020-02-07 08:40:41
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# zip

## 概要

- zip是内置函数，可以压缩列表、字典、集合等

## 解析

- zip返回的是一个zip对象，需要通过for循环来读取
- zip的元素都是元组
- 当多个序列中元素个数不一致时，会以最短的序列为准进行压缩
- `list(zip(list1, list2))` 读取zip对象
```python
a=[11,12,13]
b=(21,22,23)
[x for x in zip(a,b)] # [(11, 21), (12, 22), (13, 23)]

dic={31:2, 32:4, 33:5}
set1={41,42,43,44}
[x for x in zip(dic, set1)]
#[(31, 41), (32, 42), (33, 43)]
[x for x in zip('hello', 'wmsj100')]
#[('h', 'w'), ('e', 'm'), ('l', 's'), ('l', 'j'), ('o', '1')]
```


## 参考

- [python zip](http://c.biancheng.net/view/2237.html)
