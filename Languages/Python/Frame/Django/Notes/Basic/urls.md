---
title: urls
date: 2018-05-01 16:10:50 Tue
modify: 2020-02-13 12:50:24 
tag: [urls]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

# 路由设置

## 概述

- 设置路要页面

## 正则路由

- 如果路由中要写正则，则不能再使用`path`，需要更换为`re_path`
```path
from django.urls import path, re_path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1_views.index),
    re_path(r'^add/$', app1_views.add, name='add'),
    re_path(r'^add2/(\d+)/(\d+)/$', app1_views.add2, name='add2'),
]
```

## url调用
- Django可能会存在很多个app，每个app可能会出现路由名称name值相同的情况，这样使用变量url时候就会出错
- `<a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>`
- 这样就需要在app的对应urls.py文件中添加命名空间
- `app_name='polls'`
- 模板使用时候`{% url 'polls:detail' question.id %}`
