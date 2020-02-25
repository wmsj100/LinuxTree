---
title: 测试代码
date: 2018-05-01 21:26:14 Tue
modify: 2020-02-23 08:51:20 
tag: [tests]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

# 关于测试

## 概述

- 测试将节约时间，有时候会觉得和富有创造性和生产力的业务代码比起来，编写枯燥的测试代码实在太无聊了，特别是当知道代码完全没有问题的时候。
- 然后编写测试用例还是要比花费几小时手动测试应用，或者是为了找到某个小错误而胡乱翻看代码要有意义的多。
- 测试不仅能发现错误，还可以预防错误
- 测试使代码更有吸引力，其他开发者希望正式使用你的代码前看到它通过了测试。
- 测试有利于团队协作
- 测试驱动开发

## 之前对测试的误解

- 都在强调测试代码的重要性，即便它时冗余的，但只要还是有效的，
- 测试代码可以写完就忘记存在，因为只要不出错，说明要测试的代码正确工作。
- 现在感觉和测试代码的距离还很遥远，当务之急是先把逻辑代码写完整

## 测试流程

- 编写测试代码，在app目录下的tests.py
```python
from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() return False for questions whoes pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```
- `python manage.py test polls` 开始执行测试
- 测试打印
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/ubuntu/Github/python_study/django/study6/polls/tests.py", line 15, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
- 解析测试流程
	- `python manage.py test polls`将会寻找polls的全部测试代码
	- 找到了`django.test.TestCase`的一个子类
	- 创建一个特殊的数据库供测试使用
	- 在类中寻找测试方法，以test开头的方法
	- 在`test_was_publisted_recently_with_future_qustion`中创建实例
	- 使用`assertIs()`期望返回False，

- test的client.get的response
```response
[{'True': True, 'False': False, 'None': None}, {'csrf_token': <SimpleLazyObject: <function csrf.<locals>._get_val at 0x7fad01524a60>>, 'request': <WSGIRequest: GET '/test1/'>, 'user': <SimpleLazyObject: <function AuthenticationMiddleware.process_request.<locals>.<lambda> at 0x7fad015249d8>>, 'perms': <django.contrib.auth.context_processors.PermWrapper object at 0x7fad0150c8d0>, 'messages': <django.contrib.messages.storage.fallback.FallbackStorage object at 0x7fad014e6978>, 'DEFAULT_MESSAGE_LEVELS': {'DEBUG': 10, 'INFO': 20, 'SUCCESS': 25, 'WARNING': 30, 'ERROR': 40}}, {}, {'paginator': None, 'page_obj': None, 'is_paginated': False, 'object_list': <QuerySet []>, 'recently_questions': <QuerySet []>, 'view': <test1.views.IndexView object at 0x7fad014e69b0>}]
```
