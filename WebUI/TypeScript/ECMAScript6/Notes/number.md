---
title: 数值的扩展 
date: 2018-06-26 22:03:00	
modify: 
tag: [number]
categories: ES6
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数值的扩展

## 概述
- `Number.isFinite()` 判断一个值是否时有限值;
- `Number.isNaN()`; 判断一个值是否时`NaN`
- `Number.parseInt(), Number.parseFload()` 只接受字符串参数;把`ES5`的全局的`parseInt/ parseFloat`移到`Number`对象上面
- `Number.isInteger()` 判断一个数值是否为整数;
	- Number.isInteger(1.0); // true;
	- JS内部,整数和浮点数采用的是同样的存储方法,所以`25`和`25.0`被视为同一个值.
	- 25 === 25.0 ; // true
- `Number.EPSILON` 获取js表示的最小精度,小于这个值就不能精确表示了,没有意义了.
- `Number.MAX_SAFE_INTEGER/Number.MIN_SAFE_INTEGER` 表示js能精确表示的极限
- `Number.isSafeInteger()` 判断一个整数是否在极限范围内;

## Math扩展的字段
- `Math.trunc` 去除一个数的小数部分,可以接受非数值
- `Math.sig()` 判断一个数到底是正数/负数/零,分别返回`1/-1/0`,对于无法转换数值的返回`NaN`

## 新增
- `**` 表示指数运算符

## 参考
- []()
