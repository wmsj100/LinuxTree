---
title: include
date: 2018-04-30 19:52:44 Mon
modify: 2018-04-30 19:52:44 Mon
tag: [basic]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

## 概述
- include函数允许引用其他`URLconfs`，函数的正则表达式不具有`$`，而是尾部斜线，每当`Django`遇到include时，将删除于此匹配的URL部分，并将剩余的字符串发送到包含的URLconf进行进一步处理。

## 范例
- url(r'^polls/', include('polls.urls'))
