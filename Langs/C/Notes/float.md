---
title: float小数
date: 2019-04-13 20:42:15	
modify: 
tag: [float]
categories: C 
author: wmsj100
mail: wmsj100@hotmail.com
---

# float小数

## 概述
- 小数有俩种表示方法，一种是正常的小数形式
- 指数形式: 用e/E来表示10 2.1E5 == 2.1*10^5  \*
- float: 单精度浮点型 固定占位4位
- double: 双精度浮点型 固定占位8位
- float/double默认都保留6位小数，不足六位以0补齐，超过6位四舍五入
- 小数压根不能精确存储，所以不能精确输出

## 字符
- %f: 十进制输出float
- %lf 十进制输出double
- %e: 以指数形式输出float，输出结果中e小写
- %E: 以指数形式输出float，输出中E大写
- %le: 以指数输出double，e小写
- %lE: 以指数输出double，E大写
- %g: 以占位最短的方式输出小数，可能是数学表示，也可能是科学计数，e小写
- %lg: 灵活输出double，e小写
- %G: 灵活输出float，E大写
- %lG: 灵活输出double，E大写

## 默认类型
- 整数默认都是int类型
- 小数默认都是double类型
- long a = 100; 需要先将100从int类型转换位long类型，然后赋值给变量a；
- int a = 100; 不需要进行类型转换就可以直接赋值
- float a = 1.23; 需要先将1.23从double类型转换为float类型，然后赋值给变量a
- double a = 1.23; 这个就不需要类型转换

## 默认后缀
- 100l/L 表示long类型
- 1.23f/F 表示float类型

## float和int转换
- 小数和整数可以互相转换，
- float=> int 去掉小数部分
- int => float 整数后面加0

## 参考
- [小数](http://c.biancheng.net/cpp/html/3093.html)
