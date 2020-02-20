---
title: 闭包
date: 2020-01-12 12:27:20
modify: 2020-02-20 13:14:44 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 闭包

## 概要

- 一个函数调用的结果是另一个函数，这样的函数就被称作闭包
- 每次调用外部函数，内部函数都会被重新绑定，
- 闭包就是引用了自由变量的函数，这个函数保存了执行的上下文，可以脱离原本的作用于独立存在。

## 经典闭包

```python
def fn():
    msg = 'hello word'

    def fn1():
        return msg

    return fn1

a = fn()
print(a())
```

## 范例

- 幂的闭包,感觉这也是解释闭包的很经典的方法
```python
def fn(n):
    def fn2(m):
        return m**n
    return fn2

pinf = fn(2)
lif = fn(3)

print(pinf(5))
print(lif(5))
```

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

