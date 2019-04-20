---
title: 创建pythonapp
date: 2018-05-04 15:55:11 Fri
modify: 2018-05-04 15:55:11 Fri
tag: [app]
categories: Python
author: wmsj100
mail: wmsj100@hotmail.com
---

# 创建app

## 概述
- 这个文档是学习Django生成app的内容，因为是通用知识，所以导出来了。
- 在Django中创建app是很轻松的事情，但是创建完成后如何发布，如何保存，如何共享给别人，这个确实是很困惑的事情。

## 步骤
- 安装`pip`和`setuptools`
- 创建目录`django-polls`，并进入目录
- 创建`README.rst`内容如下：
```README.rst
=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
            ...
            'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

   url(r'^polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
```

- 创建`LICENSE`，公开的代码必须要有许可证，否则就毫无用处
- 创建`setup.py`
```setup.py
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
	    'Framework :: Django',
		'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
	    'Intended Audience :: Developers',
	    'License :: OSI Approved :: BSD License',  # example license
	    'Operating System :: OS Independent',
	    'Programming Language :: Python',
		# Replace these appropriately if you are stuck on Python 2.
	    'Programming Language :: Python :: 3',
	    'Programming Language :: Python :: 3.4',
	    'Programming Language :: Python :: 3.5',
	    'Topic :: Internet :: WWW/HTTP',
	    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)	
```
- 创建`MANIFEST.in`用于包含额外的文件
```MANIFEST.in
include LICENSE
include README.rst
recursive-include polls/static *
recursive-include polls/templates *
recursive-include docs *
```
- 运行`python setup.py sdist`命令构建包

## 使用自己的包
- pip install django-polls/disk/django-polls-0.1.tar.gz
- 这样就安装了包，运行`Django`的服务，可以看到`polls`应用可以正常使用了
