---
title: response
date: 2020-02-19 18:27:26
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# response

## 概要

- 每个view对象必须返回一个`HttpResponse`对象

## render

- `from django.http import render`
- 从服务器提取数据，填充到模板，渲染一个页面然后返回给浏览器
- render(request, temp_name, [content])
- content是一个可选的字典，

## redirect

- `from django.shortcuts import redirect`
- 用于页面跳转
- 可传参数
	- 一个模型，将调用模型的get_absolute_url()函数
	- 一个视图，可以带有参数，将使用urlresolvers.reverse来反向解析名称
		- `return redirect('some-view-name', foo='bar')`
	- 一个绝对路径或相对url，将原封不动的作为重定向的位置
		- `return redirect('/some/url/')

## 参考

- [diango response](https://www.django.cn/course/show-9.html)
