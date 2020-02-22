---
title: install_app
date: 2020-02-22 18:32:35
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# install_app

## 概要

- 创建app后要如何插入app呢，老方法就是在setting的`INSTALLED_APPS`中添加app的名称`polls`

## 新方法

- 新版本在app的目录下会生成一个`apps.py`的文件，这个文件专门用来管理app的名称
```apps.py
from django.apps import AppConfig

class PollsConfig(AppConfig):
    name = 'polls'
```
- 在setting中添加的方法如下
- polls.apps.PollsConfig

```python
INSTALLED_APPS = [
    'polls.apps.PollsConfig', # 新增方法
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
]
```

- 这样可以很方便的修改app的名称而不用去修改setting的配置文件，
- django中的app是支持热插拔的。

## 参考

