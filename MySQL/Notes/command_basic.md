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

## 删除表的一行数据
- delete from t1 where id=4;  删除表中id值为4的一行，
	- 如果没有where约束，就会删除整个表的数据
