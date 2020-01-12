---
title: range
date: 2020-01-11 18:05:02
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# range

## 概要

- 自动生成一个数字范围的迭代器

## 用法

- range(10) [0-9]
- range(1,10) [1-9]
- range(1,10,2) [1,3,5,7,9] 以2为步进
- range(9,1,-1) [9,8,7,6,5,4,3,2] 倒叙返回，不包括1

## 模仿实现range

- 自己实现range功能
```python
def interval(start,stop=None, step=1):
    if stop is None:
        start,stop = 0, start
    result = []

    index = start;
    while index < stop:
        result.append(index)
        index += step
    return result

print(interval(5))
print(interval(5, 10))
print(interval(1, 10, 3))
```

## 参考

