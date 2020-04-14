---
title: orm
date: 2020-02-20 17:14:44
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# orm

## 概要

- ORM: Object Relational Mappint 对象关系映射
- 面向对象编程和关系型数据库，都是目前最流行的技术，但是它们的模型是不一样的。
- 面向对象编程把所有的实体看成对象(object),关系型数据库则是采用实体之间的关系连接数据。
- 关系也可以用对象表达，这样的话，就能使用面向对象编程，来操作关系型数据库。
- ORM: 就是通过实例对象的语法，完成关系型数据库的操作的技术，是对象-关系映射的缩写
- 数据库的表(table) --> 类(class)
- 记录(record, 行数据) --> 对象(object)
- 字段(field) --> 对象的属性(attribute)
- ORM使用了对象，封装了数据库操作，因此可以不碰SQL语言。
- 开发者只使用面向对象编程，与数据对象直接交互，不用关心底层数据库
- ORM优点
	- 数据模型都在一个地方定义，更容易更新和维护，也利于重用代码
	- ORM有现成的工具，很多功能都可以自动完成，比如数据消毒、预处理、事务等等
	- 它迫使你使用MVC架构，ORM天然就是Model，最终使代码更清晰
	- 基于ORM的业务代码比较简单，代码量少，语义性好，容易理解。
	- 你不必编写性能不佳的SQL。
- ORM的缺点:
	- ORM库不是轻量级工具，需要花费很多精力学习和设置
	- 对于复杂的查询，ORM要么是无法表达，要么性能不如原生SQL。
	- ORM抽象掉了数据库层，开发者无法了解底层的数据库操作，也无法定制一些特殊的SQL。
- 是python封装的用来操作数据库的API

## 写数据库

- 写如数据库的方法有三种
	- `Article.object.create(title='ss', content='xxx')`
	- `a=Article(); a.save()`
	- `Article.object.create(**dict)`

## 修改值

- `Article.objects.filter(title='新增标题1').update(title='我被修改类')`

## 查询

- 

## 参考

- [django orm)](https://www.django.cn/course/show-18.html)
- [阮一峰的ORM](http://www.ruanyifeng.com/blog/2019/02/orm-tutorial.html)
