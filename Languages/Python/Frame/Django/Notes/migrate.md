---
title: migrate
date: 2020-02-19 21:05:15
modify: 2020-02-25 16:08:04 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# migrate

## 概要

- 数据库的操作

## 删除数据库

- 通过django创建的数据库如果只是在mysql中手动删除是无法重新通过`python manage.py makemigration/migrate`来重新生成的。
- 手动删除app目录下的migrations目录的文件，然后再重新执行生成，也无效
- 解决方法：
	- 手动删除app生成的表
	- 数据库创建和生成的记录全部记录在表格django_migrations
	- 清除表django_migrations中关于blog的app的信息
	- `delete from django_migrations where app='blog';`
	- `python manage.py makemigrations`
	- `python manage.py migrage`
	- 然后就可以重新生成数据库了。

- 也可以从一个app导入另一个app数据，但是需要修改导出的json文件的model的名称，然后导入就成功了。
- 也可以通过mysql来操作。

## 参考

