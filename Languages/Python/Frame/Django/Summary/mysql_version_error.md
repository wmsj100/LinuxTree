---
title: django的pymysql报version版本错误
date: 2020-03-02 10:44:35
modify: 
tags: [Summary]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# django的pymysql报version版本错误

## 概要

- django通过pip安装了pymysql后启动项目报错
- `django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.`

## 解决

- 查找资料说那是当前这个版本的django的一个bug
- `django-admin --version` 3.0.2
- 找到这个文件，然后注释代码
- `vi /home/pi/Software/virtualenv/lib/python3.7/site-packages/django/db/backends/mysql/base.py`
```
version = Database.version_info
# if version < (1, 3, 13):
#     raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```
- 注释这个版本判断的逻辑，然后重启项目

## 参考

