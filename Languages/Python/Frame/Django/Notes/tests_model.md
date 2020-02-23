---
title: model的test测试
date: 2020-02-23 10:11:23
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# model的test测试

## 概要

- 这个是模块的测试

## 代码

- 测试设置了3个边界值，分别是早于timezone.now(),晚于一天的，一天的最后一秒
- 我之前就是从事测试工作，这个应该是得心应手的
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

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23,
                minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
```

## 参考

