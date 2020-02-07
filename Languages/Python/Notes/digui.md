---
title: 递归
date: 2020-01-12 14:17:53
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 递归

## 概要

- 常见的递归就是阶乘和幂运算
- 阶乘最经典就是通过递归来实现
- 凡是可以通过递归实现的都可以通过循环来实现
- 递归一定要向已知方向行进

## 典型递归范例

```python
"""
f(0) = 1，f(1) = 4，f(n + 2) = 2*f(n+ 1) +f(n)，其中 n 是大于 0 的整数
"""

def fn(n):
    if n == 0:
        return 1
    elif n == 1:
        return 4
    else:
        return 2*fn(n-1) + fn(n-2)

print(fn(10)) #10497

"""
f(20) = 1，f(21) = 4，f(n + 2) = 2*f(n+ 1) +f(n)，其中 n 是大于 0 的整数
"""

def fn2(n):
    if n == 20:
        return 1
    elif n == 21:
        return 4
    else:
        return fn2(n+2) - 2*fn(n+1)

print(fn2(10)) #-70592323
```

## 阶乘

- 递归实现
```python
def jiechen(n):
    if n <= 1:
        return 1
    else:
        return n*jiechen(n-1)

print(jiechen(5))
```
- 循环实现
```python
def fn(n):
    result = 1
    for num in range(n):
        result *= n
        n -= 1
    return result

print(fn(5))
```
```python
def fn(n):
    result = n
    for num in range(1,n):
        result *= num
    return result

print(fn(5))
```

## 幂运算

- 循环实现
```python
def power1(m,n):
    result = 1
    for i in range(n):
        result *= m
    return result
```
- 递归实现
```python
def power2(m,n):
    if n == 0:
        return 1
    else:
        return m * power2(m,n-1)
```

## 参考

