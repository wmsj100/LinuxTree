---
title: sqlalchemy
date: 2020-09-14 10:14:55
modify: 
tags: [Libs]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# sqlalchemy

## 概要

- 是一个python的orm库，可以用来管理常见的数据库，包括oracle，
- 如果是oracle，依赖与oracle客户端提供的动态库，需要提前在环境配置动态库的环境变量

## oracle

- 对于oracle依赖于cx_oracle库，需要提前通过pip安装
```python
from sqlalchemy import create_engine
engin = create_engine('oracle+cx_oracle://JIAYAN:jiayan@xx.xx.xx.xx:1522/orcl',encoding='utf8',echo=True)
conn = engin.connect()
aa=con.execute("select name,value from v$parameter where name ='db_block_size'")
aa.fetchall()
# [('db_block_size', '8192')]

```

## 参考

