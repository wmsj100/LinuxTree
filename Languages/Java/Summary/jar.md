---
title: jar
date: 2020-06-08 18:31:47
modify: 
tags: [Summary]
categories: Java
author: wmsj100
email: wmsj100@hotmail.com
---

# jar

## 概要

- jar包本身是跨平台的，所以它是没有什么平台的比如x86等约束的。
- 但是jar包可能会依赖C的动态库，如果是这样的，那这样的jar包就需要修改动态库为平台可用的才可以使用
- 有些jar本身就是跨平台的，内部的动态库是按照平台来加载的，可能对于平台支持的不是非常完整。

## 参考

