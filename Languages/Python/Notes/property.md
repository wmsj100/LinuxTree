---
title: property
date: 2020-01-15 07:43:52
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# property

## 概要

- 之前访问和设置类的属性，通过都是通过方法来实现(fget, fset)等自定义方法。
- 在新式类中可以通过`property`来实现这一步骤，而且操作更简单，
- 应该使用property来替换访问器

## property介绍

- property可以有4个参数，分别是fget/fset/fdel/doc
	- fget: 设置参数只读
	- fset: 设置参数可写
	- fdel: 设置删除特性
	- doc:  文档字符串

## property使用
```python
class Size(list):
    def __init__(self, *args):
        super(Size, self).__init__(*args)
        self.width = 10
        self.height = 15

    def getSize(self):
        return self.width, self.height

    def setSize(self, size):
        self.width = size[0]
        self.height = size[1]

    size = property(getSize, setSize)
#>>> import magic4
#>>> a=magic4.Size()
#>>> a
#[]
#>>> a.
#a.append(   a.count(    a.height    a.pop(      a.setSize(  a.width
#a.clear(    a.extend(   a.index(    a.remove(   a.size
#a.copy(     a.getSize(  a.insert(   a.reverse(  a.sort(
#>>> a.size
#(10, 15)
#>>> a.width
#10
#>>> a.height
#15
#>>> a.size=[30,45]
#>>> a.size
#(30, 45)
#>>> a.width
#30
#>>> a.height
#45
#>>> a.getSize()
#(30, 45)
#>>> a.setSize([55,77])
#>>> a.getSize()
#(55, 77)
#>>> a.size
#(55, 77)
#>>> a.width
#55
#>>> a.height
#77
```

## 参考

