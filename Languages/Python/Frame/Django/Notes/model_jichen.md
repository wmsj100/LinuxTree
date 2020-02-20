---
title: model继承
date: 2020-02-20 11:52:57
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# model继承

## 概要

- django中的model是可以继承的，这样大量重复性的字段申明可以提取到common中，然后每个class继承common

## 使用

- 要实现抽象基类必须申明`abstrate=True`的Meta类
```python
class CommonInfo(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        abstract = True

class People(CommonInfo):
    sex = models.CharField(max_length=10)

class People2(CommonInfo):
    lever = models.CharField(max_length=10)
```
- 这样创建并迁移数据库后就可以在mysql数据库中看到创建的表格
```mysql
mysql> desc myblog_people;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| name  | varchar(20) | NO   |     | NULL    |                |
| age   | int(11)     | NO   |     | NULL    |                |
| sex   | varchar(10) | NO   |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

mysql> desc myblog_people2;
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| name  | varchar(20) | NO   |     | NULL    |                |
| age   | int(11)     | NO   |     | NULL    |                |
| lever | varchar(10) | NO   |     | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```
## 参考

- [django model继承](https://www.django.cn/course/show-15.html)
