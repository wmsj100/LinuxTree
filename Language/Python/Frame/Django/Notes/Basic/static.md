---
title: 静态文件
date: 2018-05-01 22:38:21 Tue
modify: 2018-05-01 22:38:21 Tue
tag: [static]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

# 静态文件

## 概述
- 在新创建的app内创建`static/polls`，所有的静态文件放置到此位置，
- 静态文件也存在有命名空间的问题
- 通过加载`static`模块就可以使用`static`变量
```html
{% load static %}
 <link rel="stylesheet" type="text/css" media="screen" href="{% static 'polls/css/style.css' %}" />
```
- 对于css文件，是分开好还是直接就写在一个文件中好，肯定是分开好，因为一个文件对于修改和查找太恐怖了。

## 范例
