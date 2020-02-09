---
title: __slots__
date: 2020-02-09 11:02:15
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# __slots__

## 概要

- 限制给对象实例添加属性或方法
- 该限制只作用于当前类。
- 是一个元组结构，只能添加或定义列出的字符串的属性或方法名
- `__slots__ = ('name', 'age')`

## 范例

```python
class People:
    __slots__ = ('name', 'age')

class chen(People):
    pass
```

## 参考

- [python __slots__](http://c.biancheng.net/view/2291.html)
