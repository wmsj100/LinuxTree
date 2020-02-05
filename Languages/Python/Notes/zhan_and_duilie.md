---
title: 栈和队列
date: 2020-02-05 10:11:03
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 栈和队列

## 概要

- 队列和栈是俩种数据结构，其内部都是按照固定顺序来存放变量的，二者的区别在于对数据的存取顺序
- 队列: 先存入的数据先取出，即"先进先出"
- 栈: 后存入的数据先出，即“后进先出”

## python的list模拟队列

- 使用`insert`在list的首位插入数字
- 使用`pop`来获取末尾的数字

## 模拟栈

- 使用`append`插入值
- 使用`pop`取出值

- 通过list可以模拟值，但是insert插入值的效率并不高，因为每次从列表的开头插入一个数据，列表中所有的元素都得向后移动一个位置。

## collections模块

- `collections.deque` 是一个特殊结构体，被设计成在俩端存入和读取都很快的特殊list，用来实现栈和队列的功能。
``python
import collections
a = collections.deque()
a.append(1)
a.append(2)
a.append('hello')
a # deque([1, 2, 'hello'])
# 模拟队列
a.popleft() # 1
# 模拟栈
a.pop() # 'hello'
a # deque(['hello'])
```

## 参考

- [python list实现队列和栈](http://c.biancheng.net/view/vip_5999.html)
