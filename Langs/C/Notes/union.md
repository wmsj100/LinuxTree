---
title: union共用体
date: 2019-04-23 23:09:15	
modify: 
tag: [union,basic]
categories: C
author: wmsj100
mail: wmsj100@hotmail.com
---

# union共用体

## 概述
- 结构体和共用体的区别在于：结构体的各个成员会占用不同的内存，互相之间没有影响；
- 共用体的所有成员占用同一段内存，
- 共用体使用了内存覆盖技术，同一时刻只能保存一个成员的值，如果对新的成员赋值，会把原来成员的值覆盖掉
- 共用体在一般的编程中应用较少，在单片机中应用较多

## 参考
- []()