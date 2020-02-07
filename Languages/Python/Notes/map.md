---
title: map
date: 2020-01-12 21:49:24
modify: 2020-02-07 21:38:59 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# map

## 概要

- map函数的功能是对可迭代对象中的每个元素都调用指定的函数，并返回一个map对象。
- 返回的map对象不能直接输出，可以通过for循环或list函数来显示。
- 返回的map对象也只能被读取一次，
- map函数直接用C语言写成，运行时不需要通过python解释器间接调用，并且内部做了诸多优化，所以相比其他方法，此方法的运行效率最高
- 多结合lambda来使用
- map函数将序列中的所有元素全部传递给一个函数
- `list(map(str, range(10)))` ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
- map生成的也是一个可迭代对象

## 范例

- map传入一个list的范例
- `b=map(lambda x:x*2, a)` # list a的每个元素都\*2

- map传入多个可迭代对象作为参数
```python
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
c = list(map(lambda x,y:x+y,a,b))
c # [4, 6, 8, 10, 12]
```

## 参考

- [Python map](http://c.biancheng.net/view/vip_6064.html)
