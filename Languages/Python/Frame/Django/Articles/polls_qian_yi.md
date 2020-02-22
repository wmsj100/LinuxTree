---
title: polls项目迁移
date: 2020-02-22 21:22:14
modify: 
tags: [Articles]
categories: Django
author: wmsj100
email: wmsj100@hotmail.com
---

# polls项目迁移

## 概要

- 之前一直在强调Django是一个支持热插拔的框架，其实对于热插拔根本就没有太多理解
- 刚刚因为学习官方教程在study4项目写，但那个项目有定时任务读取疫情的接口在跑，害怕日志被弄乱，所以就想到了要迁移到新目录study5，
- 迁移过程异常的简单，直接把polls复制到study5，
- 在setting文件插入polls
- 修改urls文件，因为polls的路由
- 从study4把polls的数据库数据dumpdata出来，
- study5 loaddata进去数据
- 重启study5项目，
- polls页面查看成功
- 这样就一个app迁移完成，是完全俩个不同的项目，这一点让我很惊讶。
- 所以这就是django的设计哲学，这是需要好好学习的。

## 参考

