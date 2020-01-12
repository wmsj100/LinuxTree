---
title: 闭包
date: 2020-01-12 12:27:20
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 闭包

## 概要

- 一个函数调用的结果是另一个函数，这样的函数就被称作闭包
- 每次调用外部函数，内部函数都会被重新绑定，

## 范例

- 手动实现乘法的闭包
```python
def fn1(num):
    def fn2(num2):
        return num*num2
    return fn2

print(fn1(5))
print(fn1(5)(3))
```

## 参考

