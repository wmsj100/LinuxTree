---
title: lambda
date: 2020-02-07 17:33:35
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# lambda

## 概要

- lambda又称为匿名函数，常用来表示内部仅包含1行表达式的函数。
- 如果一个函数的函数体仅有1行，则该函数就可以用lambda表达式来代替

## 使用

- `add = lambda x,y:x+y` 这样就定义了一个add函数，返回俩个数的和
- 如果要用普通函数，需要3行才可以定义，lambda使用一行就可以了。
- `lambda`表达式其就是简单函数，函数体的简写版本

## 优势

- 对于单行函数，使用lambda表达式可以省去定义函数的过程，让代码更加简洁
- 对于不需要多次复用的函数，使用lambda表达式可以再用完之后立即释放，提高程序执行的性能。

## 参考

- [python lambda](http://c.biancheng.net/view/2262.html)
