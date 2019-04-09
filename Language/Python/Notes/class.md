---
title: 类
date: Sun 31 Dec 2017 11:50:57 AM CST
modify: 2019-04-09 19:45:20	
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础概念
- 在python中所有的数据类型都可以视为对象，也可以自定义对象，这种数据类型就是面向对象中的类
- class 定义类需要使用
- 静态变量: 通过类调用的变量为静态变量，所有的实力都共享
- 私有变量: 变量名称前面有俩个下划线`self.__id = id`，私有变量只能在类内部调用，不能通过对象来调用

## 继承
- 继承: 类之间可以实现继承，子类通过`super`方法来调用父类的方法, python版本不一样，super的调用方法不一样
	- python3: super().__init__(id,name,age)
	- python2: super(Chen, self).__init__(id, name, age)
	- python2: Hero.__init__(self, id, name, age)

- `__init__` 类实例化操作会自动为新创建的类实例调用`__init__`方法

- 当一个类继承另一个类时，它将继承父类的所有功能（变量和方法）。

- 定义类的时候可以选择要继承的类，默认时继承`object`,也可以自定义要继承的类`Person`

- del 删除对象，如果对象的引用计数器变为零时，垃圾回收会删除这个对象

