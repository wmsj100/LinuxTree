---
title: 类
date: Sun 31 Dec 2017 11:50:57 AM CST
modify: 2020-01-12 23:03:44 
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础概念

- 在python中所有的数据类型都可以视为对象，也可以自定义对象，这种数据类型就是面向对象中的类
- class 定义类需要使用
- 静态变量: 通过类调用的变量为静态变量，所有的实例都共享
- 私有变量: 变量名称前面有俩个下划线`self.__id = id`，私有变量只能在类内部调用，不能通过对象来调用，或者通过`a._Person__name`实例_ClassName__privateName这样的方式也可以访问私有变量
- 类命名空间: 所有位于class语句的代码都在特殊的命名空间，这些属性和方法可以被所有实力访问。

```python
__metaclass__=type

class Person:
    __name="" # 私有属性
    count = 1 # 公共属性

    def init(self):
        Person.count += 1 # 通过这个方法会修改所有实力的属性名count的值

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def greet(self):
        print('Hello,world! I\'m %s' % self.__name)
```

- 类的三个属性是“多态/封装/继承”

## 判断实例是否拥有属性

- hasattr(a, 'talk') 判断实例a是否拥有属性`talk`,不关心判断的属性是变量还是方法
