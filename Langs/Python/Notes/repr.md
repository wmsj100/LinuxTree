---
title: repr
date: 2019-04-11 16:28:20	
modify: 
tag: [Note]
categories: Python 
author: wmsj100
mail: wmsj100@hotmail.com
---

# repr

## 概述
- repr函数得到的字符串通常可以用来重新获取该对象，
- 他可以把任何python数据类型转换为字符串，
- 通过eval方法重新转换可以得到一个深拷贝
- a = eval(repr(b)) a就是b的一个深拷贝
- a = eval(str(b)) 
- 它和str功能类似，但是比str更友好

## 参考
- [repr解析](https://www.cnblogs.com/itdyb/p/5046415.html)
