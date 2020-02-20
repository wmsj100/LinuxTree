---
title: orm_dates
date: 2020-02-20 18:18:31
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# orm_dates

## 概要

- 返回特定类型的所有可用日期

## 使用

- `Article.objects.dates('create_time', 'year')` 返回所有不同年份的列表
- `Article.objects.dates('create_time', 'month')` 返回所有不同年/月的列表
- `Article.objects.dates('create_time', 'day')` 返回所有不同年/月/日的列表
- `Article.objects.dates('create_time', 'day', order='DESC')` 返回所有不同年/月/日的列表, 逆序排列

## 参考

- [django orm_dates](https://www.django.cn/course/show-18.html)
