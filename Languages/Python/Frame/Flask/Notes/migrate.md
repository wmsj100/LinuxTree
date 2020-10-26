---
title: migrate
date: 2020-10-26 11:11:26
modify: 
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# migrate

## 概要

- flask-migrate的数据库版本管理工具，当进行表变更，尤其是包含主键的表进行名称变更或者删除操作时候可能会报错。
- 即便是在mysql中进行`drop table project_database_relase_veify`删除表的操作的时候也会报错，
- 重启docker-compose的所有容器，其实主要是重启mysql，然后执行回退操作，手动删除表格，总之可以这样尝试来实现表的操作的顺利执行，不能出现异常后就执行`python run.py db stamp head`这样来规避报错，这样的后果就是不能实现mysql的平滑升级

## 参考

