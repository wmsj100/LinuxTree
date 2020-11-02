---
title: query
date: 2020-11-02 14:11:00
modify: 
tags: [Notes]
categories: Oracle
author: wmsj100
email: wmsj100@hotmail.com
---

# query

## 概要

- 查询oracle数据库sql

## 分页查询前100条数据，按照primary_key排序

- `sql = f'SELECT * FROM (SELECT {column_sql} FROM {owner}.{table_name} ORDER BY {primary_key_sql}) table_alise where rownum <=per_page'`
- `sql = f'SELECT * FROM(SELECT "TARGET_TABLE".*, ROWNUM "TARGET_ROWNUM" FROM(SELECT {column_sql} FROM {owner}.{table_name} ORDER BY {primary_key_sql}) "TARGET_TABLE" WHERE ROWNUM <= 100) WHERE "TARGET_ROWNUM" >= 1'`
- `sql = f'SELECT {column_sql} FROM {owner}.{table_name} ORDER BY {primary_key_sql}'`

## 参考

