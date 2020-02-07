---
title: partial偏函数
date: 2020-02-07 15:38:40
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# partial偏函数

## 概要

- 它是对原始函数的二次封装，是将现有函数的部分参数预先绑定为指定值，从而得到一个新的函数，该函数就称为偏函数。
- 相比原函数，偏函数具有较少的可变参数，从而降低了函数调用的难度。
- `partial`偏函数需要使用该关键字

## 用法

```python
"""
偏函数练习
"""
from functools import partial

def my_add(m,n):
    return m+n

my_add_5 = partial(my_add, m=5)

print(my_add_5(n=8)) # 必须使用关键字传参
print(my_add(5,8))

def class_info(level, count):
    return '{} level has student\'s count is {}'.format(level, count)

class_two_info = partial(class_info, level='two')

print(class_two_info(count=20))
print(class_info('two', 20))
```

## 参考

- [python partial偏函数](http://c.biancheng.net/view/vip_6060.html)
