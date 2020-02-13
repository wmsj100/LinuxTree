---
title: templates
date: 2020-02-13 12:51:19
modify: 
tags: [Basic]
categories: Notes
author: wmsj100
email: wmsj100@hotmail.com
---

# templates

## 概要

- 存放模板文件的位置

## 操作

- 为每个app创建目录`app/templates/app`，这样可以避免模板名称和其他app的模板重复导致查找文件出错
- 调用或者引入模板都需要添加app名称`{% extends 'app1/base.html' %}` `return render(request, 'app1/home.html')`
- 再`base.html`可以通过`{% include 'app1/nav.html' %}` 导入文件

## 参考

- [django 模板](https://code.ziqiangxuetang.com/django/django-template.html)
