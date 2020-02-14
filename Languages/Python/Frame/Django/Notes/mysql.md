---
title: mysql
date: 2020-02-14 18:45:53
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# mysql

## 概要

- django链接mysql真的是简单的不可思议，为什么当时就没有去操作一下，
- 以为mysql深奥的不行，这些配置别人都做好了，只需要照搬就好，当时杜斌勇应该就是这样操作的。

## 配置

- 配置`setting.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django1',
        'USER': 'ubuntu',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}
```
- 修改`study2/__init__.py`，引入mysql的驱动
```python
# coding=utf-8
#
import pymysql
pymysql.install_as_MySQLdb()
```
- 在确保数据库中已经存在目标数据库后生成数据库
- `python manage.py makemigrations`
	- 报错，提示mysqlclient版本太低，这是bug，可以注释掉相关代码
	- `/home/ubuntu/Code/Python/virtual/py3env/lib/python3.6/site-packages/django/db/backends/mysql/base.py`
```python
# version = Database.version_info
# if version < (1, 3, 13):
#     raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```
- `python manage.py migrage` 生成表
- 去数据库查看生成的表
```
mysql> show tables;
+----------------------------+
| Tables_in_django1          |
+----------------------------+
| auth_group                 |
| auth_group_permissions     |
| auth_permission            |
| auth_user                  |
| auth_user_groups           |
| auth_user_user_permissions |
| blog                       |
| django_admin_log           |
| django_content_type        |
| django_migrations          |
| django_session             |
+----------------------------+
```
- 链接数据库mysql完成

## 参考

- [mysql+django](https://blog.csdn.net/topqy/article/details/89336720)
