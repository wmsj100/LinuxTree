---
title: 索引
date: 2019-04-09 23:06:02	
modify:
tags: [index]
categories: MySQL
---

# 索引

- 索引是一种与表有关的结构，相当于书的目录，可以根据目录的页码快速找到所需的内容。
- 当表中有大量的记录时，若要对表进行查询，没有索引会是全表搜索；将所有记录一一取出，然后和查询条件进行一一对比，然后返回满足条件的记录。
- 这样做会消耗大量的数据库系统时间，并造成大量的磁盘I/O操作。

- 如果有索引值，会先和索引中找到符合条件的索引值，通过索引值就可以快速找到表中的数据，大大加快搜索速度。
- 索引的效率取决于索引列是否散列，即该列如果越不相同，那么索引的效率越高

## 创建索引
- alter table employee add index idx_id(id);
- create index idx_name on employee(name); 给employee表的name列创建idx_name索引

## 创建唯一索引
- 在设计数据表的时候，看上去唯一的列都可以添加这个约束
- alter table student add unique index uni_name(name); 给name列添加唯一索引，name列不允许出现重复值
- alter table student add constraint uni_name unique (name) 只创建唯一约束，不创建唯一索引

## 查询索引
- show index from employee;
- 在使用select语句查询的时候，语句中where里面的条件，会自动判断有没有可用的索引。

## 删除索引
- alter tabel student drop index idx_id; 删除索引idx_id

## 总结
- 无论是否创建索引，对用户和应用程序来说，使用关系型数据库是没有任何区别的，这个是对数据库有意义的操作，如果有索引，数据库就通过索引查询数据，如果没有索引，查询也能正常进行，只是速度会慢。
