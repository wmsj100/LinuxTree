---
title: pymysql
date: 2019-04-09 12:38:52	
modify: 
tag: [model]
categories: Python 
author: wmsj100
mail: wmsj100@hotmail.com
---

# pymysql

## 概述
- 这个是python用来连接mysql的模块

## 使用
- 连接数据库

```python
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='testdb',
    charset='utf8'
)
```

- 创建游标
```python
cursor = connect.cursor()
# 插入数据
sql = "insert into student values('test', 23)"
cursor.execute(sql)
cursor.execute('select * from student')
print cursor.fetchall()
connect.commit() # 默认修改不会提交到数据库，需要手动提交
cursor.close()
connect.close() # 关闭连接

## 参考
- [pymysql](https://www.cnblogs.com/DswCnblog/p/6208726.html)
