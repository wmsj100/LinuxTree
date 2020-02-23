---
title: 通过setuptools发布应用
date: 2020-02-23 16:05:36
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# 通过setuptools发布应用

## 概要

- Django本来就是支持热插拔的，但是假如一个应用已经完善，如何分发这个应用
- 使用setuptools

## 步骤

> Django的官方例子polls应用打包

- 在非当前工程目录创建目录`django-polls`
- 复制`polls`到目录`django-polls`
- 写README.rst
```README.rst
=====
Polls
=====

Polls is a Django app to conduct Web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
```
- 添加`LICENSE`授权证书
- 添加文档说明目录`docs`
- 添加`MANIFEST.in`
```MANIFEST.in
include LICENSE
include README.rst
recursive-include polls/static *
recursive-include polls/templates *
recursive-include docs *
```
- 创建`setup.cfg`
```setup.cfg
[metadata]
name = django-polls
version = 0.1
description = A Django app to conduct Web-based polls.
long_description = file: README.rst
url = https://www.example.com/
author = Your Name
author_email = yourname@example.com
license = BSD-3-Clause  # Example license
classifiers =
    Environment :: Web Environment
    Framework :: Django
    Framework :: Django :: X.Y  # Replace "X.Y" as appropriate
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Operating System :: OS Independent
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Topic :: Internet :: WWW/HTTP
    Topic :: Internet :: WWW/HTTP :: Dynamic Content

[options]
include_package_data = true
packages = find:
```
- 添加`setup.py`
```setup.py
from setuptools import setup

setup()
```
- 执行`python setup.py sdist`在当前目录打包应用，这样将在当前目录创建一个dist目录`django-polls-0.1.tar.gz`
- 这样应用就可以分发了，
- `python -m pip install --user django-polls-0.1.tar.gz`  非虚拟环境用户
- `python -m pip install django-polls-0.1.tar.gz`  虚拟环境用户
- 重启django服务，就可以正常使用了
- `python -m pip uninstall django-polls` 卸载

## 参考

- [Django polls打包](https://docs.djangoproject.com/zh-hans/3.0/intro/reusable-apps/)
