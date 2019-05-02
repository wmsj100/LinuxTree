---
title: shell运算
date: 2019-04-12 14:38:49	
modify: 2019-05-02 10:00:21	
tag: [expr]
categories: Shell 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 运算

## 概述
- expr将它的参数当作一个表达式来求值，
- 它的功能非常强大，可以完成许多表达式的求值运算
- expr命令通常被替换为更有效的`$((1+2))`
- shell的四则运算通过`expr`来实现
- 运算符前后必须添加空格
- `*` 必须进行转义
- 支持的运算包括`|,&,=,>,>=,<,<=,!=,+,-,*,\,%`

## 范例
```sh
a=`expr 1 + 2`
a=`expr 1 - 2`
a=$(expr 1 \* 2)
a=$(expr 1 / 2)
a=$(expr 1 % 2)
a=$(expr $b + $c)
```

## 参考
- [expr运算](http://c.biancheng.net/cpp/view/2736.html)
