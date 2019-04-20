---
title: 表格
date: 2019-04-09 22:15:26	
modify:
tags: [Basic]
categories: MySQL
---

# 表格信息

## 增加
- create table shop1 like shop; 基于表ship创建一个类似的空白表
- create table shop2 select * from shop; 完全克隆shop包括表结构和数据

## 删除
- drop database 用于丢弃数据库中所有表格，并且删除数据。
- drop index idx_id on person; 从表person中删除索引
- drop table tst1,tst2,tst3; 一次性删除表tst1/2/3
- insert into student (name) values('wmsj100'),('小明'),('小李'); 一次性插入多条数据
- delete from student; 删除表中所有数据
- delete from student where id!=3; 删除表格中除id=3外的所有数据

## 修改
- alter table shop1 rename shopp1; 重命名表格
- alter table student add class_id int default 1; 给表格添加列class_id,默认值为1
- alter table student modify class_id int(10); 修改表格student的class_id列的特性
- rename table shop2 to shopp2;	重命名表格
-  update student set class_id=1 where name=wmsj100; 修改表的值

## 查找
- show create table pet; 查看表格的创建信息
- desc pet; 查看表格的信息，用表格形式展示；
- select databese(); 获取数据库的名称；
- show index from pet; 查询pet的索引情况，其中可以看到pet的一些信息，包括total等值。
- do 用于执行表达式，但是不返回任何结果。
	- do sleep(5); 只是等待5s后执行，但是没有结果返回，
	- select sleep(5); 等待5s后执行，而且会方法一个记录
- analyze table shop； 分析表shop
- check table shop; 检查表，
- show character set; 展示所有可用的字符集
- show columns from shop; ==> desc shop; 显示表结构信息
- show create database test; 显示创建数据库信息
- show engines; 显示所有引擎
- show errors; 显示
- show grants for 'wmsj'@'localhost' 列出用户的信息
