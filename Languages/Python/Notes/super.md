---
title: super
date: 2020-02-09 09:14:58
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# super

## 概要

- 父类的构造方法子类同样会继承。
- python是一门支持多继承的面向对象的编程语言
- 子类对象在调用该方法时，会优先选择排在最前面的父类中的实例方法，构造方法也是如此。

```python
class People:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("I am people {}".format(self.name))

class Animal:
    def __init__(self, food):
        self.food = food

    def eat(self):
        print("I eat food {}".format(self.food))

class Anys(People, Animal):
    pass
a = Anys('wmsj')
a.eat() # error
```
- 上面这个代码中，当实例化`Anys`这个类时，因为继承的俩个父类都有各自的构造方法，所以默认只执行第一个父类的构造方法。把第二个类Animal的构造方法遮蔽了。
- `a=Anys('wmsj100')`，如果执行`a.eat()`就会报错，提示找不到`food`
- 如何选择实例化俩个父类的构造方法呢
- 接近方法就是使用`super`，这个也只能调用第一个父类的构造方法。
- 第二个父类的构造方法还需要通过`Animal.__init__(self, food)`
- 代码修改如下
```python
class People:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("I am people {}".format(self.name))

class Animal:
    def __init__(self, food):
        self.food = food

    def eat(self):
        print("I eat food {}".format(self.food))

class Anys(People, Animal):
    def __init__(self, name, food):
        super().__init__(name)
        Animal.__init__(self, food)
a = Anys('wmsj', 'mianbao')
a.food # 'mianbao'
a.name # 'wmsj'
```

## 参考

- [python super函数](http://c.biancheng.net/view/2290.html)
