---
title: property
date: 2020-01-15 07:43:52
modify: 2020-02-08 16:15:19  
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
- 使用property就是为了保证类的封装，类包含的属性应该是隐藏的，只允许通过类提供的方法来间接实现对类属性的访问和操作。

## property介绍

- property可以有4个参数，分别是fget/fset/fdel/doc
	- fget: 设置参数只读
	- fset: 设置参数可写
	- fdel: 设置删除特性
	- doc:  文档字符串

- 通过使用如下
	- `name = property(getname, setname, delname) 给name完整的访问、修改、删除方法
	- `name = property(getname, setname)` name只有访问和修改方法，没有`del obj.name`方法，不支持这样调用，但是可以通过`obj.delname()`这样调用

## property使用

- 其实之前就有学到这个方法，当时没有留下深刻印象，现在才意识到它是真的有用的。
- 下面这个`__name`是私有属性，本来是无法直接修改的，但是通过`property`给绑定到类`name`中，所以通过name这个变量间接实现了修改访问和删除

```python
class Cls3:
    def __init__(self, name):
            self.__name = name
    def getname(self):
            return self.__name
    def setname(self, name):
            self.__name = name
    def delname(self):
            self.__name = 'xxx'
    name = property(getname, setname, delname, 'show use')

a = Cls3('wmsj100')
a.name # 'wmsj100'
a.name = 'wanghao'
a.name # 'wanghao'
del a.name
a.name # 'xxx'

```

## 参考

- [python property](http://c.biancheng.net/view/2286.html)
