---
title: flask-sqlalchemy-uuid-duplicate
date: 2020-09-16 21:26:33
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# flask-sqlalchemy-uuid-duplicate

## 概要

- 使用flask-sqlalchemy连接数据库，想要创建一个默认字段id，是通过uuid来获取值的，而且是设置为主键的，primary key
- 使用uuid的时候出现的一个问题是uuid会重复，可能第一次计算的值和第三次计算的值是相同的，导致插入的数据因为主键重复无法插入。
- 后来被迫使用了autoincrement自增长字段才解决了这个问题。
- 我在想是因为我的sqlalchemy设置的有问题，还是怎么，反正计算的uuid就是有问题。或者再试一次创建时候直接创建id值来,不要使用默认的字段类型。是不是因为默认的值的缓存问题导致的。

## 解决

- 问题是由于id是通过models自动创建的，现在修改为创建project时候手动创建id的uuid值，这样可以保证值是相同的，我在想一下，我报错重复的uuid值是uuid1和uuid4都尝试过，就是因为在models设置导致的，所以现在放到controllers中就避免了重复，而且现在使用uuid1的值
- 现在class都通过继承来使用common的值

## 参考

