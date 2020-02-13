---
title: 表单
date: 2018-05-01 16:30:52 Tue
modify: 2018-05-01 16:30:52 Tue
tag: [form]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

# 表单模块

## 概述
- 对于表单，如果是修改数据库内容，`method="post"`
- 为了防止跨站点请求伪造，使用`{% csrf_token %}`模板标签
- `request.POST`是一个类似于字典的对象，可以通过关键字获取提交的数据，返回一个字符串
- `request.GET`用来访问GET数据
