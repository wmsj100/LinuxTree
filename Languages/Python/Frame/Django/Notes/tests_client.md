---
title: tests_client
date: 2020-02-23 12:59:16
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# tests_client

## 概要

- 测试用例执行过程中可以模拟用户点击页面
- 继承自TestCase
- `response = self.client.get(url)` 模拟访问url

## 范例

```python
from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse

# Create your tests here.

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date = time)

class QuestionResultViewTest(TestCase):
    def test_question_empty_choice(self):
        question = create_question(question_text='one question.', days=-1)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_question_contain_choice(self):
        question = create_question(question_text='one question.', days=-1)
        question.choice_set.create(choice_text='choice value is ok', votes=0)
        url = reverse('polls:results', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'choice value is ok')
```


## 参考

