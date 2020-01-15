---
title: 生成器
date: 2020-01-15 09:29:18
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 生成器

## 概要

- 生成器和迭代器是python最重要的俩个概念
- 生成器可以创建一个迭代器
- 生成器是一个包含`yield`关键字的函数,当它被调用时，在函数体中的代码不会被执行，而是返回一个迭代器。
- 生成器是由俩部分组成的，生成器的函数和生成器的迭代器。
	- 生成器函数：由def定义的包含yield的部分
	- 生成器的迭代器: 函数的返回部分。

## 创建

- 解包一个二元list[[1,2],[3,4],[5]]
```python
class Flatten:
    def __init__(self):
        pass

    def flatten(self, list):
        for sublist in list:
            for element in sublist:
                yield element

#>>> a=shengchengqi.Flatten()
#>>> b=a.flatten([[1,2],[3,4],[5]])
#>>> b
#<generator object Flatten.flatten at 0x765ddb30>
#>>> next(b)
#1
#>>> next(b)
#2
#>>> c=list(b)
#>>> c
#[3, 4, 5]
```

## 递归生成器

- 上面的生成器只能解包俩层，可以通过递归来解多层
```python
class Digui:
    def __init__(self):
        pass

    def flatten(self, listVal):
        try:
            for sublist in listVal:
                for element in self.flatten(sublist):
                    yield element
        except TypeError:
            yield listVal
#>>> from shengchengqi import *
#>>> a=Digui()
#>>> list1=[[1],[[2,3,[4]]],[[[[5]]]]]
#>>> b=a.flatten(list1)
#>>> list(b)
#[1, 2, 3, 4, 5]
```

- 上面的生成器无法处理字符串，可以添加判断，如果是字符串，就直接`yield`，对字符串的判断可以通过直接和另一个空字符串相加，如果出现异常，说明不是字符串，反之则是字符串
```python
class Digui1:
    def __init__(self):
        pass

    def flatten(self, listVal):
        try:
            try:
                listVal + ''
            except TypeError: pass
            else: raise TypeError

            for sublist in listVal:
                for element in self.flatten(sublist):
                    yield element

        except TypeError:
            yield listVal
#>>> from shengchengqi import *
#>>> a=Digui1()
#>>> list(a.flatten(['adf', 'sss', 'ddd']))
#['adf', 'sss', 'ddd']
#>>> list(a.flatten(['adf', 'sss', ['ddd']]))
#['adf', 'sss', 'ddd']
```

## 参考

