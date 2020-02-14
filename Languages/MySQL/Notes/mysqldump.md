---
title: mysqldump
date: 2020-02-14 20:31:54
modify: 
tags: [Notes]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# mysqldump

## 概要

- 导出数据命令
- 导出操作只有root有权限

## 导出数据库指定表数据

- `sudo mysqldump django1 -u root --tables blog > /tmp/blog.sql`

## 参考

- [mysqldump导出](https://www.cnblogs.com/linjiqin/p/11888943.html)
