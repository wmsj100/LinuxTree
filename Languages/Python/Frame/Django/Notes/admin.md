---
title: admin
date: 2020-02-13 21:35:49
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# admin

## 概要

- 给app开启后台管理功能

## 操作

- 新创建的app目录内有一个`admin.py`是用来管理
```python
from django.contrib import admin
from .models import Article, Author, Tag
# Register your models here.

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Tag)
```

## 参考

