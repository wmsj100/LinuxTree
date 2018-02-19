# 基础命令

- show databases; 查看数据库
- use test; 进入数据库
- show tables; 查看表
- create database study; 创建study数据库
- create table(id int(10), name char(20), phone int(12)); 创建一个表，包含id, name, phone;
- select * from employee; 查看表的数据

## 插入数据
- insert into employee(id, name, phone) values(01, 'TOM', 110110); 向表中插入数据。
- insert into employee values(02, 'Jack', 1191119119)
- insert into employee(id, name) values(003, 'Rose'); 插入部分数据
- drop database employee; 删除数据库

## 更新表数据
- undate shirt set style='dress' where id=2;	修改表shirt的id=2的一行的style=‘dress’；

## 删除表的一行数据
- delete from t1 where id=4;  删除表中id值为4的一行，
	- 如果没有where约束，就会删除整个表的数据

## 导出mysql数据和表
- mysqldump -d study > db.sql;	导出study数据库的所有表的结构，不包含数据
- mysqldump study > db.sql; 导出数据库study的所有表结构，并且包含插入的数据；
- mysqldump 这个操作是在退出mysql控制台进行的。

- select version() 查看版本信息
- select current_date; 查看当前日期
- select current_time; 获取当前时间
- select (4-1)*5;  可以进行简单的计算
- select now(); 获取当前日期和时间；
