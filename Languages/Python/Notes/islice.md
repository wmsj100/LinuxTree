---
title: islice
date: 2020-02-21 17:28:56
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# islice

## 概要

- 迭代器的一个切片工具

## 使用

```python
from itertools import islice

a=iter(range(10))
b=islice(a, 3)
c=islice(a, 4)
list(b) # [0,1,2]
list(c) # [3, 4, 5]
list(a) # [6, 7, 8, 9]
```

- 从上面的例子可以知道`islice`会消耗迭代器

## 参考

- [python islice](https://blog.csdn.net/strive_for_future/article/details/95388081)
