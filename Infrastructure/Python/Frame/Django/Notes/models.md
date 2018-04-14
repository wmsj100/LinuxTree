---
title: Django模型
date: 2018-04-14 11:40:47 Sat
modify: 2018-04-14 11:40:47 Sat
tag: [models]
categories: Django
author: wmsj100
mail: wmsj100@hotmail.com
---

## 创建模型
- Django模型是与数据库相关的，和数据库相关的代码都放在`models.py`中
- 在models.py中创建数据库
  ```python
  from django.db import models
  class Person(models.Model):
      name = models.CharField(max_length=30)
      age = models.IntegerField()
      def __str__(self):
          return self.name
  ```
## 同步数据库
- python manage.py makemigrations
- python manage.py migrate
- `python manage.py shell` 进入shell面板
  ```python
  import learn.models import Person
  Person.objects.create(name="wmsj100", age=12)
  Person.objects.get(name="wmsj100")
  <Person: wmsj100>
  ```

## 新建一个对象的方法
1. Person.objects.create(name="wmsj100", age=12)
2. p = Person(name="wmsj100", age=12); p.save()
3. p = Person(name="wmsj100"); p.age = 12; p.save()
4. Person.objects.get_or_create(name="wmsj100", age=12) 这个方法可以避免创建重复的值，但是速度相对较慢，返回一个元组

## 获取对象
1. Person.objects.all() 获取所有值
2. Person.objects.all()[:10] 获取10个人
3. Person.objects.get(name="wmsj100") 用来获取一个对象，
4. Person.objects.filter(name="wmsj100")  过滤出所有叫wmsj100的人
5. Person.objects.filter(name__iexact="wmsj100") 不区分大小写，找出wmsj100, WMSJ100....
6. Person.objects.filter(name__contains="wmsj") 找出名称中包含wmsj的人
7. Person.objects.filter(name__icontains="WM") 找出包含wm的且不区分大小写
8. Person.objects.filter(name__regex="^wm") 正则表达式，找出wm开头的
9. Person.objects.filter(name__iregex="^WM") 正在表达式，不区分大小写，找出WM开头
10. Person.objects.exclude(name__contains="wm") 找出所有不包含wm的人
11. Person.objects.filter(name__regex="\d$").exclude(name__contains="wmsj") 找出所有以数字结尾但是不包含wmsj的人
