---
title: request
date: 2020-02-19 18:13:03
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# request

## 概要

- django的请求方法

## 常用方法

- HttpRequest请求对象是有django自动创建的
- request.path 获取url路径
- request.get_full_path() 获取完整路径，包括?page=1
- request.method = GET|POST
- request.GET 获取通过GET请求的参数 `<QueryDict: {'page': ['345']}>`
- request.GET.get('page') 获取get请求中的page参数的值
- request.POST
- request.COOKIES 获取cookie
- request.FILES
- request.user 获取当前登录用户
- request.session 唯一可读写的属性，

## 参考

- [django request](https://www.django.cn/course/show-9.html)
