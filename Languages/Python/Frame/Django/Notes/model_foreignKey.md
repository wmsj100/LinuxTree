---
title: model_datetime
date: 2020-02-22 18:00:00
modify: 2020-02-23 12:50:41  
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# model_datetime

## 概要

- 之前有用到时间这个数据格式，但没什么深刻印象，也没太当回事，
- 刚刚用时间格式进行过滤查询才感觉到很强大

## 使用

```model.py
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
```
- 在Choice表中创建一个question的外键，实际会在这个表创建一个`question_id`的字段
```mysql
mysql> select * from polls_choice;
+----+--------------------+-------+-------------+
| id | choice_text        | votes | question_id |
+----+--------------------+-------+-------------+
|  1 | Not much           |     0 |           1 |
|  2 | The sky            |     0 |           1 |
|  3 | Just hacking again |     0 |           1 |
+----+--------------------+-------+-------------+
3 rows in set (0.00 sec)
```

```python
from django.utils import timezone

current_year = timezone.now().year
Choice.objects.filter(question__pub_date__year=current_year)


```

## 外键表如何创建值

- 上面的表Choice有关联到Question外键，如何给Choice创建值呢，
- 因为Choice是关联于Question，所以就需要指定一个question的值来创建
- `a.choice_set.create/all/values` 用这样的格式来创建或查询值
```python
>>> a.choice_set.create(choice_text='Please Check', votes=3)
<Choice: Please Check>
>>> a.choice_set.create(choice_text='Dont care', votes=34)
<Choice: Dont care>
>>> a.choice_set.create(choice_text='very care', votes=0)
<Choice: very care>
>>> a.choice_set.values()
<QuerySet [{'id': 4, 'question_id': 2, 'choice_text': 'Please Check', 'votes': 3}, {'id': 5, 'question_id': 2, 'choice_text': 'Dont care', 'votes': 34}, {'id': 6, 'question_id': 2, 'choice_text': 'very care', 'votes': 0}]>
>>>

```

## 删除外键的值

- `c=q.choice_set.filter(choict_text__startswith='Just hacking')); c.delete()`
- 通过主键question的值先过滤出要删除的值，然后调用delete方法

## 模板展示外键

- `for choice in question.choice_set.all`
- 本来是需要调用`all()`方法的，但是模板中是不支持`()`，所以模板只写`all`就可以
```html
<h1>{{ question.question_text }}</h1>
<ul>
	{% for choice in question.choice_set.all %}
	<li>{{ choice.choice_text }}</li>
	{% endfor %}
</ul>
```

## 查询关联外键的值

- Choice中的question外键到Question
- 现在想查询所有包含choice的question，这个怎么实现，一次查询肯定做不到，
- 需要先统计Choice中包含的question.id,使用集合推导式，获取到所有id的集合
- 然后通过上面统计的出的id进行filter过滤
```python
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        choice_question_set = {
                choice.question_id for choice in Choice.objects.all()
                }
        return  Question.objects.filter(id__in=choice_question_set)
```

## 参考

- [django文档](https://docs.djangoproject.com/zh-hans/3.0/intro/tutorial02/)
