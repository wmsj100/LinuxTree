---
title: Django官方文档测试案例
date: 2020-02-23 12:52:43
modify: 
tags: [Storage]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# Django官方文档测试案例

## 概要

- 这是Django的官方案例
- 写test的过程中有一些自己的思考

## 总结

- 写代码过程中思路会跟随着变化，这个变化很频繁，
- 但是每一次变化如果都有写测试用例，这个变化就会慎重一些，不会很随意的就进行一些破坏性的变更，
- 因为要修改的测试用例也太多了。
- 本来是要写没有创建choice的question，在results页面不展示，
- 过程中就变更为question的index和vote页面也不展示，
- view代码已经修改完成了，然后执行测试用例发现一大片报错，然后就想着是不是不需要那样大范围更改
- 只是限制在results页面就可以，
- 然后重新回退view的修改代码，只是修改result对应的代码
- 测试用例全部执行通过

## 测试用例代码

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


class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future question.', days=30)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are avaliable.")
        self.assertQuerysetEqual(
            response.context['last_questions'], []
                )

    def test_past_question(self):
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
                response.context['last_questions'], ['<Question: Past question.>']
        )

    def test_future_question(self):
        create_question(question_text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are avaliable.')

    def test_future_question_and_past_question(self):
        create_question(question_text='Future question.', days=30)
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['last_questions'], ['<Question: Past question.>']
        )

    def test_two_past_question(self):
        create_question(question_text='Past question 1.', days=-30)
        create_question(question_text='Past question 2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['last_questions'], 
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
                )



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

- [django test](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial05/)
