---
title: 基础知识
date: 2018-04-30 18:09:10 Mon
modify: 2018-04-30 18:09:10 Mon
tag: [django]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# Django基础知识

## 概述
- Django自带了一个开发服务器，使用纯python开发的轻量级web服务器，只用于开发，不能用于生产环境

## 命令
- python manage.py runserver 8080
- django-admin startproject mysite 创建项目
- python manage.py startapp polls 创建polls应用
- url('^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),在views中的参数必须和`question_id`保持一致

## 设置
- TIME_ZONE='Asia/Shanghai' # 设置时区为上海
- LANGUAGE-CODE='zh-ch' # 设置语言为中文

## 通用视图
- 根据URL中的参数从数据库中获取数据，载入模板文件然后返回渲染后的模板，
- 通用视图期望从URL中捕获名为`pk`的主键值，因此定义url时需要写入`pk`
- `	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),`
```python
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question': question})

# 通用视图
class DetailView(generic.DetailView):
	model = Question
	template_name='polls/detail.html'
```

## 新创建app
- 新创建app后需要把`polls.apps.PollsConfig`添加到`INSTALLED_APPS`
