---
title: format
date: 2020-02-05 18:53:30
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# format

## 概要

- python后期推出的一个功能更加强大的字符串模板，通过传入的参数进行格式化，并且使用大括号作为特殊字符代替`%`

## 基本用法

- 不带编号{} 
	- `'{} is {}'.format('wmsj100', 23)` # 'wmsj100 is 23'
- 带数字编号{1},可调换顺序
	- '{0} is {1} {0}'.format('wmsj100', 32) # 'wmsj100 is 32 wmsj100'
- 带关键字{a}
	- '{a} {tom} {a}'.format(tom='wmsj100', a=23) # '23 wmsj100 23'

## 对齐方式

- < 默认，左对齐
- > 右对齐
	- '{:10s} and {:>10s}'.format('hello', 'world')
	- 'hello      and      world'
- ^ 中间对齐
	- '{:^10s} and {:^10s}'.format('hello', 'world')
	- '  hello    and   world   '

## 参考

- [format](https://www.cnblogs.com/lovejh/p/9201219.html)
