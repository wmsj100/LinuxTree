---
title: 断言
date: 2020-01-11 17:30:26
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 断言

## 概要

- 如果出现错误就直接让程序奔溃
- 并且抛出指定的错误类型

## 用法

- `assert 1<a<10, 'a must little then 10'` 如果a大于10，程序就会报错
```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: age must little then 30
```

## 参考

