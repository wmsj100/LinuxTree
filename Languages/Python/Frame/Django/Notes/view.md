---
title: view
date: 2020-02-22 18:57:26
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# view

## 概要

- 视图是**一类具有相同功能和模板的网页的集合**
- 一个博客应用中可能会创建如下几个视图
	- 博客首页--展示最近的几项内容
	- 内容详情页--详细展示某项内容
	- 以年为单位的归档页--展示选中的年份里各个月份创建的内容
	- 以月为单位的归档页--展示选中的月份里各天创建的内容
	- 以天为单位的归档页--展示选中的天里创建的所有内容
	- 评论处理器--用于响应为一项内容添加评论的操作。

## 常用方法

- `django.shortcuts`模块中有很多常用方法
- `from django.shortcuts import render, get_object_or_404` 
	- render 渲染模板
	- `get_object_or_404`: 查询model使用get方法，如果没有值就返回404
	- `get_list_or_404`	: 查询model使用filter，为空就返回404

## 设计哲学

- 为什么我们使用辅助函数`get_object_or_404`而不是自己捕获异常呢，还有为什么模型api不直接抛出ObjectDoesNotExist而是抛出Http404呢？
- 因为这样做会增加模型层和视图层的耦合性。
- 指导Django设计的最重要的思想之一就是要保证松散耦合。

## 参考

- [view](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial03/)
