---
title: processlist
date: 2020-03-11 14:00:54
modify: 
tags: [Notes]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# processlist

## 概要

- 查看当前数据库的连接数,
- root用户可以看到所有用户的连接数
- 其他用户只能看到自己账户的所有连接数

## 使用

- `show processlist;`
```
mysql> show processlist;
+------+---------+--------------------+---------------+---------+------+----------+------------------+
| Id   | User    | Host               | db            | Command | Time | State    | Info             |
+------+---------+--------------------+---------------+---------+------+----------+------------------+
| 1046 | wmsj100 | 111.18.94.29:17554 | django_study4 | Sleep   | 5440 |          | NULL             |
| 1058 | wmsj100 | 111.18.94.29:17256 | django_study4 | Sleep   | 1033 |          | NULL             |
| 1064 | root    | localhost          | NULL          | Query   |    0 | starting | show processlist |
| 1067 | wmsj100 | 111.18.94.29:17266 | django_study4 | Sleep   |   99 |          | NULL             |
| 1081 | wmsj100 | 111.18.94.29:17219 | django_study4 | Sleep   |   43 |          | NULL             |
| 1083 | wmsj100 | 111.18.94.29:17221 | django_study4 | Sleep   |   31 |          | NULL             |
+------+---------+--------------------+---------------+---------+------+----------+------------------+
6 rows in set (0.00 sec)
```

## 参考

- [mysql查看最大连接数](https://www.cnblogs.com/caoshousong/p/10845396.html)
