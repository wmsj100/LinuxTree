---
title: Django模型
date: 2018-04-14 11:40:47 Sat
modify: 2020-02-13 19:06:32 
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

1. `Person.objects.all()` 获取所有值
2. `Person.objects.all()[:10]` 获取10个人
3. `Person.objects.get(name="wmsj100")` 用来获取一个对象，
4. `Person.objects.filter(name="wmsj100")`  过滤出所有叫wmsj100的人
5. `Person.objects.filter(name__iexact="wmsj100")` 不区分大小写，找出wmsj100, WMSJ100....
6. `Person.objects.filter(name__contains="wmsj")` 找出名称中包含wmsj的人
7. `Person.objects.filter(name__icontains="WM")` 找出包含wm的且不区分大小写
8. `Person.objects.filter(name__regex="^wm")` 正则表达式，找出wm开头的
9. `Person.objects.filter(name__iregex="^WM")` 正在表达式，不区分大小写，找出WM开头
10. `Person.objects.exclude(name__contains="wm")` 找出所有不包含wm的人
11. `Person.objects.filter(name__regex="\d$").exclude(name__contains="wmsj")` 找出所有以数字结尾但是不包含wmsj的人
12. `Person.objects.all().order_by("name")` 按照名称排序
13. `Person.objects.all().order_by("-name")` 按照名称逆序

## 数据库外键

- 数据库外键是通过id来关联的，
- `author = models.ForeignKey(Author, on_delete=models.CASCADE)`
- 会在当前表中自动添加一个`author_id`来关联到`Author的id中，
- 在这个表中可以通过`author__name/email/addr`这样的方式访问Author表中的任意字段
```python
a = Article.objects.all().first()
a.author_id
a.author.name
a.author.email
```

## 数据库常见运算

- `from django.db.models import Count`  总数
- `from django.db.models import Sum` 求和
- `from django.db.models import Avg` 平均值
## 数据库常用命令

- `str(Author.objects.all().query)` 
- 获取元组形式的值
	- `Author.objects.values_list('name', 'qq')` 获取元组形式结果 `<QuerySet [('wmsj100', '5829662795'), ('wmsj', '7455737170'), ('wanghao', '3729797385'), ('heian', '5147903322')]>`
	- `Author.objects.values_list('name', flat=True)` 获取一个字段的数组 `<QuerySet ['wmsj100', 'wmsj', 'wanghao', 'heian']>`
	- `Article.objects.filter(author__qq='5829662795').values_list('title', 'content')`
	- `Article.objects.filter(author__name='wmsj100').values_list('title', flat=True)` 查找wmsj100的所有文章，并且列出title
	- 关于外键可以通过`author__name`来调用`Author`的所有值，因为外键是链接的整个表。
- 获取字典形式的值
	- `Author.objects.values('name', 'qq')` `<QuerySet [{'name': 'wmsj100', 'qq': '5829662795'}, {'name': 'wmsj', 'qq': '7455737170'}, {'name': 'wanghao', 'qq': '3729797385'}, {'name': 'heian', 'qq': '5147903322'}]>`
	- `Article.objects.filter(author__name='wmsj100').values('title')` 获取wmsj100的所有文章的title字典列表 
	- `<QuerySet [{'title': 'Django_1'}, {'title': 'Django_2'}, {'title': 'Django_3'}, {'title': 'Django_4'}, {'title': 'Django_5'}, {'title': 'Django_6'}, {'title': 'Django_7'}, {'title': 'Django_8'}, {'title': 'Django_9'}, {'title': 'Django_10'}, {'title': 'Django_11'}, {'title': 'Django_12'}, {'title': 'Django_13'}, {'title': 'Django_14'}, {'title': 'Django_15'}, {'title': 'Django_16'}, {'title': 'Django_17'}, {'title': 'Django_18'}, {'title': 'Django_19'}, {'title': 'Django_20'}, '...(remaining elements truncated)...']>`
- 设置别名
	- `Tag.objects.all().extra(select={'tag_name': 'name'}).defer('name')` 把tag表中的name转为tag_name,这样俩个值都可以查询
- 聚合计数、求和、平均数
	- `Article.objects.values('author_id').annotate(count=Count('author')).values('author_id', 'count')` 获取每个作者的文章总数 
	- `<QuerySet [{'author_id': 13, 'count': 11}, {'author_id': 14, 'count': 16}, {'author_id': 15, 'count': 12}, {'author_id': 16, 'count': 9}, {'author_id': 17, 'count': 12}]>`
	- `Article.objects.values('author__name').annotate(count=Count('author')).values('author__name', 'count')` 统计作者名称和文章数目
	- 上面实际是操作来俩张表，具体命令`.query.__str__()`如下
	- `'SELECT "app1_author"."name", COUNT("app1_article"."author_id") AS "count" FROM "app1_article" INNER JOIN "app1_author" ON ("app1_article"."author_id" = "app1_author"."id") GROUP BY "app1_author"."name"'` 
- 获取作者的文章平均分数
	- `Article.objects.values('author__name').annotate(score=Avg('score')).values('author__name', 'score')` 具体SQL如下
	- `'SELECT "app1_author"."name", AVG("app1_article"."score") AS "score" FROM "app1_article" INNER JOIN "app1_author" ON ("app1_article"."author_id" = "app1_author"."id") GROUP BY "app1_author"."name"'`
- 求作者所有文章的总分
	- `Article.objects.values('author__name').annotate(total=Sum('score')).values('author__name', 'total')`

## 数据库优化

- `select_related`优化一对一，多对一查询
	- `a=Article.objects.all().select_related('author').first()` 
	- `a.author.email` 这样不会再次进行查询动作
- `prefetch_related` 优化一对多，多对多查询
	- `Article.objects.all().prefetch_related('tags').first()'
	- `a.tags.all()` 查询每篇文章对应的所有标签。

## defer 排除

- `Author.objects.defer('name')` 排除name
- `'SELECT "app1_author"."id", "app1_author"."qq", "app1_author"."addr", "app1_author"."email" FROM "app1_author"'`

## only 仅选择需要

- `Author.objects.only('name')` 仅选择name
- `'SELECT "app1_author"."id", "app1_author"."name" FROM "app1_author"'`

## 数据库表结构变更

- django现在自动表结构变更需要重新生成
- `python manage.py makemigrations` 如果是有新增字段，django会自动提示新增字段的默认值
- `python manage.py migrate app1 003` 把app1的数据库结构回退到003版本。

## 参考

- [djando 数据库](https://code.ziqiangxuetang.com/django/django-models.html)
- [django 数据库操作](https://code.ziqiangxuetang.com/django/django-queryset-api.html)
- [django 数据库深入解析](https://code.ziqiangxuetang.com/django/django-queryset-advance.html)
