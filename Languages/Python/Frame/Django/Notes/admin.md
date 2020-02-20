---
title: admin
date: 2020-02-13 21:35:49
modify: 2020-02-20 17:05:27 
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

## 注册admin方法

- 一种就是上面那种通过通过传参来注册
- 装饰器注册
```python
from django.contrib import admin
from .models import Article, Tags, Category

admin.site.register(Tags)
admin.site.register(Category)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title', 'intro','category', 'tags', 'user', 'create_time') # 表格显示列的内容
    list_per_page = 50 # 每页显示列数
    ordering = ('-create_time',) # 按照创建时间排序
    list_editable = ['title', 'user'] # 可以直接在列表进行修改
    fk_fields = ['category'] # 显示外键
    list_display_links = ('id', 'title') # 点击列表可以进入详情页面
    search_fields = ['title'] # 显示搜索框，
    list_filter=['user']
    date_hierarchy = 'create_time' # 显示日期过滤
```
- 通过`list_display`可以定制后台的article列表要显示的内容

## 参考

