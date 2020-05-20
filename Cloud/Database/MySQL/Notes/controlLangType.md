---
title: 控制语句类型
date: 2020-05-20 10:13:41
modify: 
tags: [Notes]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# 控制语句类型

## 概要

- mysql的控制类型有4种，DDL，DML，DCL，TCL

## 详细

- TCL: Transaction Control Language 事务控制语言
- DML: data manipulation language, 它们是select/update/insert/delete4条命令用来对数据库里的数据进行操作的语言。
- DDL: data definition language create/alter/drop等，DDL主要用来定义或者改变表结构，数据类型，表之间的链接和约束等初始化工作上。
- DCL: data control language 数据库控制功能，用来设置或更改数据库用户或角色权限的语句，包括grant/deny/revoke等，只有sysadmin/dbcreator/db_owner/db_securityadmin等人员才有权利执行

## 参考

- [mysql ddl/dml/dcl/tcl区别](https://blog.csdn.net/u012732259/article/details/39524405)
