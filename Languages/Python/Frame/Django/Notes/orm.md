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
