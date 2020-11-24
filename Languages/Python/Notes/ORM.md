---
title: orm
date: 2020-11-24 16:09:04
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# orm

## 概要

- orm: `Object Relational Mapping` 对象关系映射
- 是一种程序设计技术，在面向对象编程语言中有涉及，
- 面向对象是从软件工程基本原则(耦合、聚合、封装)的基础上发展起来的，
- 关系数据库是从数学理论发展起来的。
- ORM就是为了解决面向对象编程和关系数据库的交互而出现的。
- `python`中的orm有`sqlalchemy`，而对应到`flask`框架中就有`flask-sqlalchemy`

## 总结

- orm避免了直接在程序中硬编码sql的尴尬，而且orm针对不同数据库已经做了处理，同个orm可以对接不同的数据库存储，而几乎不需要对代码层有什么改动。
- 就像之前的校验工具使用sqlite3作为存储时候专门管理的一个sql文件，对于不同列查询时候的sql拼接也是比较痛苦的

## 参考

