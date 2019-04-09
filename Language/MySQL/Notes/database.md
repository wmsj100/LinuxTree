---
title: 数据库
date: 2019-04-09 22:05:12	
modify: 
tag: [database]
categories: MySQL
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数据库

## 概述
- create database test; 这样默认创建的数据库字符集不是utf8
- alter datebase test character set utf8; 这样修改字符集为utf8;
- 在数据库下创建的表如果不指定字符集，默认是继承数据库的字符集的，
- create table tst1(name varchar(10)) default charset utf8;
