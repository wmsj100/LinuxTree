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

## 判断父类

- `issubclass(a1, Filter)` 通过这个方法进行判断Filter是a1的基类
- a1.__bases__ 查看a1的基类
- type(a) <class 'jichen.a1'> 通过新式类创建的实例可以通过type来判断哪个类实例化的

## 多个超类

- 一个类可以继承自多个类，
- 如果多个类中有冲突的方法或者属性，那么先继承的覆盖后继承的
```python
class Cal:
    aa='cal'
    def calculate(self, value):
        self.value = eval(value)

class Talk:
    aa='talk'
    def talk(self):
        print("current value is %d" % self.value)

class test1(Cal, Talk):
    pass
a=test1()
a.aa # 'cal'
a.calculate('1+3*4')
a.talk() # 'current value is 13
```

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

