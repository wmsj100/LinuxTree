---
title: filter
date: 2020-01-12 21:53:13
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# filter

## 概要

- 可以根据一个返回布尔值的函数对一个列表进行过滤
- 返回迭代器
```python
def func(str):
	return str.isalnum()
list(filter(func,['as', '23', ',.', '*('])) # ['as', '23']
```
- 上面的例子可以通过列表推导式替代
- `[ x for x in list1 if x.isalnum() ]`

## 参考

