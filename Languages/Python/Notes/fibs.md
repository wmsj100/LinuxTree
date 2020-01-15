---
title: 斐波那契数列
date: 2020-01-15 09:03:49
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 斐波那契数列

## 概要

- 关于这个数列介绍太多了，每个编程语言都会用它来证明自己可以实现递归
- 自然界中也有很多是按照它的规律来分布的，比如向日葵/海螺/蜻蜓的翅膀/苍蝇的眼睛
- 它在数学中非常重要

## python代码实现
```python
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a,self.b = self.b, self.a+self.b
        return self.a

    def __iter__(self):
        return self

a=Fibs()

for i in a:
    if i<10:
        print(i)
    else:
        break
#1
#1
#2
#3
#5
#8
```

- python中的迭代时通过定义俩个方法来实现的，`__next__/__iter__`
