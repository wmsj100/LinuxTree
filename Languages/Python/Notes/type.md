---
title: type
date: 2020-02-09 11:09:47
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# type

## 概要

- 通常用来查看某个变量或值的类型，
- 也可以创建类

## 创建类

- `type(name, bases, dict)`
	- name: 类名称
	- bases: 一个元组，其中存储的是该类的父类
	- dict: 表示一个字典，用来表示类内定义的属性和方法

## 范例

```python
name = 'wmsj100'
age = 32
People = type('People', (object,), dict(name=name, age=age))
a = People()
a.name # 'wmsj100'
a.age # 32
```

## 参考

- [python type](http://c.biancheng.net/view/2292.html)
