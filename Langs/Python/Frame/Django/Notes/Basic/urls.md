---
title: urls
date: 2018-05-01 16:10:50 Tue
modify: 2018-05-01 16:10:50 Tue
tag: [urls]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

# 路由设置

## 概述
- Django可能会存在很多个app，每个app可能会出现路由名称name值相同的情况，这样使用变量url时候就会出错
- `<a href="{% url 'detail' question.id %}">{{ question.question_text }}</a>`
- 这样就需要在app的对应urls.py文件中添加命名空间
- `app_name='polls'`
- 模板使用时候`{% url 'polls:detail' question.id %}`
