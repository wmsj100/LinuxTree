---
title: class_jichen
date: 2020-01-12 23:22:50
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# class_jichen

## 概要

- 通过继承子类可以继承或者重构父类的属性和方法
- 继承: 类之间可以实现继承，子类通过`super`方法来调用父类的方法, python版本不一样，super的调用方法不一样
	- python3: super().__init__(id,name,age)
	- python2: super(Chen, self).__init__(id, name, age)
	- python2: Hero.__init__(self, id, name, age)

- `__init__` 类实例化操作会自动为新创建的类实例调用`__init__`方法

- 当一个类继承另一个类时，它将继承父类的所有功能（变量和方法）。

- 定义类的时候可以选择要继承的类，默认时继承`object`,也可以自定义要继承的类`Person`

- del 删除对象，如果对象的引用计数器变为零时，垃圾回收会删除这个对象

## 范例

- 继承的典型范例
```python
class Filter:
    def init(self):
        self.block = []

    def filter(self,data):
        return [ x for x in data if x not in self.block ]

class a1(Filter):
    def init(self):
        self.block = ['span']

tmpList = ['span', 'aa', 'span', 'bb']
a = a1()
a.init()
a.filter(tmpList) #['aa', 'bb']
```

