---
title: sqlalchemy
date: 2020-08-27 09:47:02
modify: 2020-10-28 19:28:01  
tags: [Notes]
categories: Flask
author: wmsj100
email: wmsj100@hotmail.com
---

# sqlalchemy

## 概要

- sqlalchemy是flask用来连接数据库的工具

## 常用操作

- `Oracle.query.filter_by(project_id = project_id).order_by(Oracle.row_num.desc())` 按照`row_num`逆序排序

## or_

```python
from sqlalchemy import or_
ProjectDatabaseRelateObjects.query.filter(or_(
			ProjectDatabaseRelateObjects.origin_id == object_item.id,
			ProjectDatabaseRelateObjects.dest_id == object_item.id

			)).delete()
```
## 参考

- [sqlalchemy notin_](https://myapollo.com.tw/zh-tw/sqlalchemy-orm-in-and-not-in-statement/)
