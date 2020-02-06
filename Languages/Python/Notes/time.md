---
title: time
date: 2020-02-03 18:33:26
modify: 2020-02-06 21:59:20  
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# time

## 概要

- 关于时间的模块

## 常用函数介绍

- time.strftime 按照规定格式来格式化时间戳
- time.localtime 返回当地时间

## 将字符串时间转换为时间戳

```python
import time

a = '2013-10-10 23:40:00'
b = time.strptime(a, "%Y-%m-%d %H:%M:%S") # 将其转换为时间数组
timeStamp = int(time.mktime(b)) # 转换为时间戳
```

## 将字符串格式更改

```python
import time
a = '2013-10-10 23:40:00'
b = time.strptime(a, "%Y-%m-%d %H:%M:%S") # 将其转换为时间数组
otherStyleTime = time.strftime('%Y/%m/%d %H:%M:%S', b) # '2013/10/10 23:40:00'
```

## 将时间戳转换为知道格式日期

```python
import time
a = 1381419600
b = time.localtime(1381419600) # 获取时间数组
otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S',b)

# 方法二
import datetime
a = 1381419600
b = datetime.datetime.utcfromtimestamp(1381419600) # datetime.datetime(2013, 10, 10, 15, 40)
otherStyleTime = b.strftime('%Y-%m-%d %H:%M:%S')
```

## 获取当前时间并转换为指定日期格式

```python
import time
now = int(time.time())
timeArray = time.localtime(now)
otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S',b)

# 方法二
import datetime
now = datetime.datetime.now()
otherStyleTime = now.strftime('%Y-%m-%d %H:%M:%S')
```

## 参考

- [python time](https://blog.csdn.net/faihung/article/details/84782822)
