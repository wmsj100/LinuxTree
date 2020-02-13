---
title: database
date: 2020-02-13 13:24:24
modify: 
tags: [Basic]
categories: Notes
author: wmsj100
email: wmsj100@hotmail.com
---

# database

## 概要

- 数据库的结构再model中设计

## 常用命令

- 创建
	- Person.objects.create(name='wmsj100', age=22)
	- a = Person(name='wmsj100', age=11) a.save()
	- a=Person(name='wmsj100'); a.age = 22; a.save()
	- Person.objects.get_or_create(name='ss', age=22)
- 查询
	- Person.objects.all()
	- Person.objects.all()[:10]
	- Person.objects.get(name='wmsj100')
	- Person.objects.filter(name='wmsj100')
	- Person.objects.filter(name__iexact='abc') 名称为abc，不区分大小写
	- Person.objects.filter(name__contains='w') 名称中包含w
	- Person.objects.filter(name__regex='^w') 正则，以w开头
	- Person.objects.filter(name__iregex='^w') 正则，以w开头,不区分大小写
	- Person.objects.exclude(name__contains='wm') 排除包含wm的所有的值
	- Person.objects.filter(name__contains='wm').exclude(age=44) 找出包含wm但排除age=44
- 删除
	- Person.objects.filter(name='heian').delete()
- 更新
	- Person.objects.filter(name='wanmei').update(email='xxx')
	- a=Person.objects.get(name='wanmei'); a.email='xxx'; a.save()
- 判断是否为空
	- Person.objects.all().exists() True/False
- 获取表的数量
	- Person.objects.count()
- 排序
	- Person.objects.all().order_by('name') 按照name排序
	- Person.objects.all().order_by('-name') 按照name逆序排序
- 去重
	- distinct()


## 参考

- [djando 数据库](https://code.ziqiangxuetang.com/django/django-models.html)
- [django 数据库操作](https://code.ziqiangxuetang.com/django/django-queryset-api.html)
