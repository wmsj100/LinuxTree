---
title: set集合
date: 2019-04-09 17:22:51	
modify: 2020-02-05 12:21:03 
tag: [basic]
categories: Python 
author: wmsj100
mail: wmsj100@hotmail.com
---

# set集合

## 概述

- 集合的特征是内部没有重复的值
- python中的集合和数学中的集合一样，用来保持不重复的元素，即集合中的元素都是唯一的。


## 使用

- 集合会将所有元素放在一对大括号中
- 集合只能存储不可变的数据类型，包括整形、浮点型、字符串、元组；
- 集合不能存储列表、字典、集合等可变的数据类型。
- set: 通过关键字`set`来创建一个集合
	- `a = set([1,2,3])`

## 集合常用方法

- `add`: 通过`add`向集合中添加值
- `remove`: 通过`remove`来删除集合中的值
- 集合只能通过循环整体读取，不能通过下标的方式来读取某个值
- `len(set_value)` 通过`len`可以获取到集合的长度
- `for`：集合可以通过`for`循环来进行值的遍历
- `clear`: 清空集合
- `copy`: 拷贝集合
- `difference` `c = a.difference(b)`将集合a中有而集合b中没有的内容赋值给集合c
- `difference_update` `a.difference_update(b)` 从集合a中删除与集合b中相同的元素
- `discard` 类似`remove` 删除集合元素
- `intersection` `c=a.intersection(b)` 取集合a和集合b的交集赋值给集合c
- `intersection_update` `a.intersection_update(b)` 取集合a和集合b的交集并更新给集合a
- `isdisjoint` `a.isdisjoint(b)` 判断a和b没有交集，如果有交集返回False, 否则返回True
- `issubset` `a.issubset(b)` 判断集合a是集合b的子集
- `issuperset` 判断是否是超级
- `pop` 取出集合一个元素
- `symmetric_difference` 取俩个集合互不相同的元素
- `union` 取俩个集合的交集
- `update` `a.update(b)` 用集合b更新集合a

## 集合运行(交集、并集、差集)

```python
a={1,2,3}
b={3,4,5}
a & b # {3}
a | b # {1, 2, 3, 4, 5}
a - b # {1, 2}
b - a # {4, 5}
```

## 参考
- [Python的常用数据结构](https://segmentfault.com/ls/1650000017333471/l/1500000016653718)
- [python set](http://c.biancheng.net/view/4400.html)
- [集合运算](http://c.biancheng.net/view/4402.html)
