---
title: setting
date: 2020-02-19 18:38:05
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# setting

## 概要

- django的设置文件

## 解析

- STATIC_URL = '/static/' 静态文件别名
- STATIC_ROOT = os.path.join(BASE_DIR,'static') 收集static文件导出的目录名称
- MEDIA_URL = '/uploads/'
- MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'uploads')

## mysql数据库配置

```conf
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_study5',
        'USER': 'ubuntu',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': 3306
    },
}
```
- 由于mysql默认引擎为MySQLdb,需要在`__init__.py`文件中添加下面代码
- python3须替换pymysql, 需要在主配置文件同级目录的__init__.py
```python
import pymysql
pymysql.install_as_MySQLdb()
````

## 参考

- [django setting](https://www.django.cn/course/show-11.html)
