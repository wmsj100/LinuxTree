---
title: property装饰器
date: 2020-02-08 16:24:44
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# property装饰器

## 概要

- 既要保护类的封装特性，又要让开发者可以使用'对象.属性'的方式操作类属性，除了使用`property`函数，还可以使用`@property`装饰器
- 通过`@property`装饰器，可以直接通过方法名来访问方法，不需要再方法名后添加一对`()`

## 代码如下

```python
class Area:
    def __init__(self, area):
        self.__area = area

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    @area.deleter
    def area(self):
        self.__area = 'xxx'

a = Area(100)
print(a.area) #100
a.area = 200
print(a.area) # 200
del a.area
print(a.area) # 'xxx'
```

## 参考

- [python @property](http://c.biancheng.net/view/vip_6068.html)
