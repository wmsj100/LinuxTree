---
title: urls
date: 2018-05-01 16:10:50 Tue
modify: 2020-02-19 17:18:49 
tag: [urls]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

# 路由设置

## 概述

- 设置路要页面

## 基础

- path中的路由可以多个path指向一个view，例如
	- `path('blog/', views.page), ` 
	- `path('blog/page<int:num>/', views.page), `
	- views.page 
		- `def page(request, num=1):` 如果num不传参，则取默认值1

## 错误页面

- 404、403、400、500等页面的默认模板可以替换，需要在django的根urls.py中设置
- 在二级app的urls中设置无效。

## url共用前缀

- 下面俩个路由共用前缀
- 对于前缀是变量的路由，在views的视图中参数必须保持一致，否则会报错传入错误参数
- 请求路由如下:
	- `http://myweb.com:8007/myblog/asdf-wmsj100/history/`
	- `http://myweb.com:8007/myblog/asdf-56/edit/`
```python
urlpatterns = [
    path('<page_slug>-<page_id>/', include([
        path('history/', views.history),
        path('edit/', views.edit),
        ])),
        ]
# views.py
def history(request, page_slug, page_id):
    return HttpResponse('history slug is {}, id is {}'.format(page_slug, page_id))

def edit(request, page_slug, page_id):
    return HttpResponse('edit slug is {}, id is {}'.format(page_slug, page_id))
```

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
- 路由的正则写法`re_path(r'articles/(?P<name>[0-9]{4})/$', views.articles)` name是组的名称，会以参数的形式传递到视图中

## 嵌套参数

- 通过正则来匹配多种路由
- 下面这条路由的正则可以匹配
	- `http://myweb.com:8007/myblog/comments/` 参数为0
	- `http://myweb.com:8007/myblog/comments/page-234/` 参数wei234
```python
    re_path(r'comments/(?:page-(?P<page_num>\d+)/)?$', views.comments),
def comments(request, page_num=0):
    return HttpResponse('page num is {}'.format(page_num))
```

## url重定向

- url重定向方便于之前保存了页签但是不至于把url\完全废弃，所以使用了重定向技术。
- 下面就是一个url的重定向，当请求
	- `http://myweb.com:8007/myblog/oldtag/oldtag_page23489/`会自动跳转到下面的链接
	- `http://myweb.com:8007/myblog/tags_page/tag-23489/`
```python
    re_path('tags_page/(?:tag-(?P<tag_num>\d+)/)?$', views.tags, name='tags'),
    re_path('oldtag/(?:oldtag_page(?P<tag_num>\d+)/)?$', views.oldtag),
# views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
def tags(request, tag_num=0):
    return render(request, 'myblog/tag.html', {'tag_num':tag_num})

def oldtag(request, tag_num):
    return HttpResponseRedirect(reverse('tags', args=(tag_num,)))
```

## url调用

- Django可能会存在很多个app，每个app可能会出现路由名称name值相同的情况，这样使用变量url时候就会出错
- `<a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>`
- 这样就需要在app的对应urls.py文件中添加命名空间
- `app_name='polls'`
- 模板使用时候`{% url 'polls:detail' question.id %}`


