---
title: about_oracle
date: 2020-11-04 11:02:29
modify: 
tags: [Summary]
categories: Oracle
author: wmsj100
email: wmsj100@hotmail.com
---

# about_oracle

## 概要

- oracle为什么这么强，因为它有很多自己的查询函数和接口，而且oracle是和硬件强耦合的，很多优化都是直接基于硬件的优化
- 比如排序使用的rownum是需要配合磁盘的排序来性能最大优化的，这和mysql只是通过软件来调度的性能优化是不可同日而语的
- 但是mysql可以胜任oracle的前提是存储换时间，mysql可以通过大量的重复存储分布式存储来实现快速的返回，
- 这个在总体上和oracle的高性能计算和低存储时间成本上是不相上下的，或者总体成本算下来要更性价比
- mysql的方式不是理论和逻辑上的最完美状态，而oracle是，但mysql是最实用的，实用为王。
- 这是我自己关于mysql可以替代oracle的一些思考。

## 参考

