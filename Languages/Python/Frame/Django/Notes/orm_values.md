---
title: orm_values
date: 2020-02-20 17:54:09
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# orm_values

## 概要

- 返回一个可以指定返回内容的字典列表
- queryset可以迭代、循环

## 使用

- `Article.objects.values()`
- `Article.objects.values('title', 'user')`
- 参与聚合应用
	- from django.db.models import Count
	- `Article.objects.values('user').annotate(count=Count('title'))` `<QuerySet [{'user_id': 1, 'count': 3}]>`
- 外键
	- `Article.objects.values('category_id')`
	- `Article.objects.values('category')`

## value_list

- 返回的不是字典，而是只包含值的元组
- `Article.objects.values_list('title', 'user')`
- `<QuerySet [('one python title', 1), ('two shell', 1), ('我被修改类', 1)]>`

## 参考

- [django orm values](https://www.django.cn/course/show-18.html)
