# 视图

- 视图是从一个表或多个表导出来的表，是一种虚拟存在的表。
- 视图属于数据库，可以使用 create view databaseName.viewName;来给指定数据库创建视图；
- 它就像一个窗口，通过这个窗口可以看到系统专门提供的数据，这样用户不用看到整个数据库的数据，而只关心对自己有用的数据。

## 注意
- 数据库中只存放了视图的定义，而没有存放视图中的数据，数据还在原来的表中存放
- 使用视图查询数据时，数据库会从原来的表中取出对应的数据
- 视图中的数据依赖于原来表中的数据，表中的数据变动，视图也会跟着变
- 在使用视图时候可以把它当作一张表

## 创建视图
- create view v_emp(v_name,v_age,v_phone) as select name,age,phone from employee;  创建视图；
- create view v_proTo1(v_pro_name, v_of_dpt, v_name, v_age) as select project.proj_name, project.of_dpt, employee.name, employee.age from project, employee where project.of_dpt = employee.in_dpt; 从俩张表中组装数据

## 修改视图
- alter view viewName;

## 删除视图
- drop view [if exists] view_name; 可以同时删除多个视图；
