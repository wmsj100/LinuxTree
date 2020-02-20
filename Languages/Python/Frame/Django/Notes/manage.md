---
title: manage
date: 2020-02-20 19:02:58
modify: 
tags: [Notes]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# manage

## 概要

- `django`的`manage.py`要脚本的功能

## 介绍

- `startproject` 创建一个项目
- `startapp` 创建一个app
- `runserver` 运行开发服务器
- `shell` 进入django shell
- `dbshell` 进入django dbshell
- `check` 检查django项目的完整性，给出优化建议
- `flush` 清空数据库
- `compilemessages` 编译语言文件
- `makemessages` 创建语言文件
- `migrate` 同步数据库
	- `python manage.py migrate` 同步数据库
	- `python manage.py migrate myblog 0001_initial` 回复数据库到指定版本
- `makemigrations` 生成数据库同步脚本
- `showmigrations` 查看生成的数据库同步脚本
- `sqlflush` 查看生成清空数据库的脚本
- `sqlmigrate` 查看数据库同步的sql语句  
	- `python manage.py sqlmigrate myblog 0001_initial`
- `dumpdata` 导出数据
- `loaddata` 导入数据
- `diffsettings` 查看当前配置和django默认配置的不同之处
- `createsuperuser` 创建超级管理员
- `changepassword` 修改密码
- `clearsessions` 清除session

## 参考

- [django manage](https://www.django.cn/article/show-26.html)
