---
title: sqlite基础知识
date: 2016-06-17
tags: [SQLite, 基础知识]
categories: Language
---

- 创建一个表的流程；
	- sqlite test2.db
	- create teble test2(id integer primary key, value text);
	- insert into test2 (value) values ('wmsj100');
	- insert into test2 (value) values ('heian');
	- insert into test2 (value) values ('hahaha');
	- insert into test2 (value) values ('dhdhdh');
	- .header on; # 显示头部
	- .mode col;	# 以列表的形式展示
	- select last_insert_rowid();	# 查看当前表格最后一个数值的索引；
	- create index test2_idx on test2(value); #创建索引
	- create view schema as select * frome sqlite_master; # 创建视图
	- .output wmsj.sql
	- .dump
	- .output stdout	# 导出数据库到文件“wmsj.sql”
	- .quit 退出sqlite数据库

- sqlite3 进入数据库，此时是一个完全空白的表，需要导入数据库文件
	- .read wmsj.sql # 读取wmsj.sql数据库文件， .read命令导入由.dump命令创建的文件。
	- .tables  # 查看当前数据库内部的所有表格文件
	- 如果要导入当前的备份文件，需要先移除已经存在的数据库对象。
	- drop table test2;
	- drop view schema;
	- .read wmsj.sql

- 格式化
	- .echo 设置新命令在执行前回显；
	- .header 查询结果显示时带有字段名
	- .nullvalue 设置NULL值的显示方式，默认是空字符，
	- .prompt  'wmsj100>' 设置命令行shell的提示符
	- .mode  设置数据的输出格式，

- 名词解析
	- 保留字： 由SQL保留用做特殊用途，如select, insert, update, delete, create, drop, begin
	- 标识符： 指明数据库里的具体对象，如表或索引，
	- sql不区分大小写
	- 保留字都用大写，标识符都用小写，
	- 单行注释用双减号开始，
	- 多行注释用/* */  C风格
	- 数据库中所有的工作都围绕表进行。
	- 表由行和列构成
	- 创建和删除数据库对象的语句一般称为数据定义语言 DDL
	- 操作这些对象中数据的语句称为数据操作语言 DML

- 创建表
	- create [temp | temporary] table_name()  
	- 用temp保留字声明的表为临时表，只存在于当前会话，一旦连接断开，就会被自动删除。
	- 中括号表示可选项
	- 竖线表示在多个中选择一个。
	- 如果没有指明创建临时表，则创建的是基本表，将会在数据库中持久存在。
	- 数据库中还有其它类型的表，如系统表和视图。
	- 创建表命令至少需要一个表名和一个字段名，
	- 字段名表示用逗号分隔的列表，
	- 每个字段定义包含一个名称、一个域和一个逗号分隔的字段约束表。
	- 域是一个类型，与编程语言中的数据类型相同。
	- SQLite中有5中本地类型： integer, real, text, blob, null
	- 约束可以控制什么样的值可以存储在表中或特定的字段中。
	- UNIQUE: 该约束来规定所有记录中某个字段的值要各不相同
	- 在字段列表后面，可以跟随一个附加的字段约束。 
	- create table contacts(id integer primary key, name text not null collate nocase, phone text not null default 'unknown', unique(name, phone));

- 改变表
	- ALTER TABLE 改变表的结构，既可以改变表名，也可以增加字段
