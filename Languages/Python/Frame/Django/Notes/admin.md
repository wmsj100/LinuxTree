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

## 设计哲学

- 为你的员工或客户生成一个用户添加，修改和删除内容的后台是一项缺乏创造性和乏味的工作。因此，Django 全自动地根据模型创建后台界面。
- Django 产生于一个公众页面和内容发布者页面完全分离的新闻类站点的开发过程中。站点管理人员使用管理系统来添加新闻、事件和体育时讯等，这些添加的内容被显示在公众页面上。Django 通过为站点管理人员创建统一的内容编辑界面解决了这个问题。
- 管理界面不是为了网站的访问者，而是为管理者准备的。

## 操作

- `python manage.py createsuperuser` 创建一个管理员
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

