---
title: filter
date: 2020-01-12 21:53:13
modify: 2020-02-07 21:51:05  
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# filter

## 概要

- filter函数的功能是对iterable中的每个元素，都使用function函数判断，并返回True/False，最后将返回True的元素组成一个新的可遍历的集合。
- 可以根据一个返回布尔值的函数对一个列表进行过滤
- 返回迭代器
```python
def func(str):
	return str.isalnum()
list(filter(func,['as', '23', ',.', '*('])) # ['as', '23']
```
- 上面的例子可以通过列表推导式替代
- `[ x for x in list1 if x.isalnum() ]`
- `list(filter(lambda x:x.isalnum(), list1))`
## 参考

- [python filter](http://c.biancheng.net/view/vip_6064.html)
