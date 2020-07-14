---
title: 内存
date: 2020-04-26 14:40:58
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# 内存

## 概要

- 内存是用来保存加载到cpu的数据，
- 函数和变量要先保存到内存才可以被执行和调用
- 如果当前函数已经被加载到内存，此时从磁盘删除该函数和变量所在文件，也不会影响函数的调用，因为此时函数已经在内存，和磁盘无关，
- 函数和方法执行完成会从堆栈中清除，下次执行再重新加载。

## 参考

- [内存](https://juejin.im/post/5d84bd1f6fb9a06b2d780df7)
