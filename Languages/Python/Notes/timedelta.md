---
title: timedelta
date: 2020-09-28 09:56:38
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# timedelta

## 概要

- 这个是datetime模块的方法，主要是获取延时时间的
- 通常在倒计时、登录session过期时间设置等

## 使用

```python
from datetime import timedelta
timedelta(hours=5)
timedelta(minutes=5)
timedelta(days=5,hours=5,minuts=5)
```

## 参考

