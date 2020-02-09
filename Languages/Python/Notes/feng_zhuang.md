---
title: 封装
date: 2020-02-08 16:34:39
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 封装

## 概要

- 简单的理解封装，即在设计类时，刻意地将一些属性和方法隐藏在类的内部，这样在使用类时，将无法直接以`类对象.属性名`或`类对象.方法名`的形式调用，而只能用未隐藏的类方法间接操作这些隐藏的属性和方法。

## 封装的好处

- 首先，封装机制保证类内部数据结构的完整性，因为使用类的用户无法直接看到类中的数据结构，只能使用类允许公开的数据，很好的避免类外部对内部数据的影响，提高类程序的可维护性。
- 除此之外，对一个类实现良好的封装，用户只能借助暴露出来的类方法来访问数据，我们只需要在这些暴露的方法中加入适当的控制逻辑，即可以避免用户对类中属性和方法的不合理操作。
- 对一个类实现良好的封装，可以提高代码的复用性

## 如何进行封装

- python类的变量和属性只有俩种类型
	- `public`: 共有属性的类变量和类方法，在类的内部、外部、以及子类中都可以正常访问
	- `private`: 私有属性的类变量和类函数，只能在本类内部使用
	- 默认情况下，python类中的变量和函数都是公有的
	- 如果类的变量和函数名称前以双下划线`__`开头，则变量为私有变量
	- `_`单下划线开头的类属性和类方法，这种类属性和类方法通常被视为私有属性和私有方法，虽然它们也能通过类对象正常访问，但这是一种约定俗成的用法。

## 参考

- [python 封装](http://c.biancheng.net/view/2287.html)