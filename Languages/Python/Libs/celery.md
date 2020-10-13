---
title: celery
date: 2020-08-27 09:44:04
modify: 2020-10-13 18:51:19  
tags: [Libs]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# celery

## 概要

- 是一个python的消息队列管理库，通常用来做消息队列的有rabbitmq和redis
- 非常好用

## 使用

```python
@celery.task(name='project_oracle_collect.controller_project_celery_task_id_create_collect', bind=True)
def controller_project_celery_task_id_create_collect(self, project_id, type):
	root_id = self.request.root_id
	controller_project_celery_task_id_create(project_id, root_id, type)
```
- bind标识绑定，然后在子任务中可以访问到父任务的`task_id`

## 参考

- [官方文档](https://docs.celeryproject.org/en/stable/userguide/tasks.html)
