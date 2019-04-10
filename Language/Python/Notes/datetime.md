---
title: datetime
date: 2019-04-10 14:15:27	
modify: 
tag: [Note]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# datetime

## 概述
- datetime模块重新封装了time模块，提供更多接口，提供的类date,time,datetime,timedelta,tzinfo

## date
```python
d1 = datetime.date(2019,04,10)
d1.year
d1.month
d1.day #年月日
d1.timestuple() #返回对应日期的time.struct_time对象
d1.weekday()	#返回周，从0开始
d1.isoweekday() #返回走，从1开始
d1.isoformat() #返回日期字符串 '2019-04-10'
```

## time
```python
t1 = datetime.time(13,22,56,111)
t1.hour # 13
t1.minute # 22
t1.second #56
t1.microsecond #111
t1.isoformat() # '13:22:56.000111'
```

## datetime
- 相当于把date和time结合起来
```python
datetime.datetime.today()
d1 = datetime.datetime.now() # datetime.datetime(2019, 4, 10, 14, 27, 43, 314000)
d1.year #2019
d1.month    #4
d1.day  #10
d1.isoweekday() #3
d1.weekday()    #2
d1.hour #14
d1.minute   #27
d1.second   #43
d1.microsecond  #314000
```

## 参考
- [datetime模块](https://www.cnblogs.com/tkqasn/p/6001134.html)
