---
title: database
date: 2020-02-14 20:16:45
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# database

## 概要

- 数据库操作

## 数据导出

- `python manage.py dumpdata` 默认导出所有表的数据
- `python manage.py dumpdata app1` 只导出app1的数据
- `python manage.py dumpdata app1 > app1_dump.json` 导出app1的数据到文件

## 数据导入

- `python manage.py loaddata blog_dump.json` 导入数据，不需要指定app

## 参考

