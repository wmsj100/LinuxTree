---
title: 类的魔法方法
date: 2020-01-13 17:11:50
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 类的魔法方法

## 概要

- 类有一些魔法方法，最常用的就是`__init__`，它是在类实例化的时候最先执行的方法
```python
class Type1:
    def __init__(self, value=123):
        self.value = value
    def show(self):
        return self.value
    def setValue(self, value):
        self.value = value
a = Type1()
a.value # 123
b = Type1('wmsj100')
b.value # 'wmsj100'
```
- 重写:类可以继承，重新继承类的方法也是一个重要机制，也可以进行扩展
- 继承超类的属性和方法: 子类继承了超类，然后实例化子类时候，查找属性和方法会先在子类中查找，然后到超类找，一级一级回溯。
- `super(ChildClass, self).__init__()`:调用未绑定的超类的方法，这样可以通过子类的实例化直接访问超类中定义的属性和方法。
```python
class Type2(Type1):
    def __init__(self, name='Type2'):
        super(Type2, self).__init__()
        self.name = name
    def sing(self):
        return self.name
```


## 参考

