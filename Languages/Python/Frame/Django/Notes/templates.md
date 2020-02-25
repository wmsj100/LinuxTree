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
- 不要在模板中写硬编码URL，这样会和url的python代码强耦合

## 操作

- 为每个app创建目录`app/templates/app`，这样可以避免模板名称和其他app的模板重复导致查找文件出错
- 调用或者引入模板都需要添加app名称`{% extends 'app1/base.html' %}` `return render(request, 'app1/home.html')`
- 再`base.html`可以通过`{% include 'app1/nav.html' %}` 导入文件
- 模板中要使用css时候需要通过`{% load static %}` 然后就可以以link的形式引入css或者图片

## 渲染变量

- 其实昨天我就有在想我在数据库中查询到的数据该怎么传输到页面呢，是必须要让值转换为`values`字典类型然后在传输吗？
- 刚刚试的结果是查询到的queryset结构也是类数组，可以在页面直接执行for循环，然后读取需要的值就可以了。

## 参考

- [django 模板](https://code.ziqiangxuetang.com/django/django-template.html)
