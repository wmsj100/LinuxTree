---
title: extern
date: 2019-04-23 19:56:31	
modify:
tags: [basic]
categories: C
---

# extern

## 概述
- extern用来指明当前的变量和函数是外部文件定义的，只是在当前文件进行函数和变量申明
- 默认定义的函数就是extern类型，即全局变量和函数，定义时候这个关键字可以省略
- 只有引用时候需要显示申明
- 函数通常是在头文件中申明的，不太会用到这个关键字吧，直接引用头文件直接用就可以
- 可能变量会用的多些