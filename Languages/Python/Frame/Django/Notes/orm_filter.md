---
title: filter操作
date: 2020-02-20 17:26:24
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# filter操作

## 概要

- filter主要用于过滤操作

## 用法

- `Article.objects.filter(id__gt=3)` 查找id大于3的
- `Article.objects.filter(id__gte=3)` 查找id大于等于3的
- `Article.objects.filter(id__lt=3)` 查找id小于等于3的
- `Article.objects.filter(id__lte=3)` 查找id小于等于3的
- `Article.objects.filter(id__gt=1,id__lt=3)` 查找id同时大于1，小于3的值
- `Article.objects.filter(id__in=[2,3])` 查找idwei2，3的值
- `Article.objects.exclude(id__in=[2,3])` 查找id不在2，3的值
- `Article.objects.filter(title__contains='one')` 查找title包含one
- `Article.objects.filter(title__icontains='one')` 查找title包含one,忽略大小写
- `Article.objects.filter(title__range=[2,3])` 查找id在范围2-3的值
- `Article.objects.filter(title__startswith='one')` 查找title以’one'开头的值
- `Article.objects.filter(title__istartswith='one')` 查找title以’one'开头的值, 忽略大小写
- `Article.objects.filter(title__endswith='title')`
- `Article.objects.filter(title__iendswith='TITLE')`
- `Article.objects.filter(title='one').order_by('title')` 排序
- `Article.objects.filter(title='one').order_by('-title')` 逆序

## 参考

- [django orm filter](https://www.django.cn/course/show-18.html)
