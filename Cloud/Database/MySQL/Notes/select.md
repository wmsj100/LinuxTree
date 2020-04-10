---
title: select
date: 2019-04-10 08:04:36	
modify: 2020-02-18 22:40:54 
tags: [basic]
categories: MySQL
---

# select 选取数据

- select name,age from employee;
- select name,age from employee where age > 25; 
- select name,age,phone from employee where name='Mary'; 查询Mary的信息
- select * from students where score!=85; 查找成绩不等于85的学生

## 投影查询
- 可以查询某几列并且设置别名
- select name n,score s from students;

## and / or
- select name,age from employee where age > 30 or age < 25; 选择年龄大于25或者小于30
- select name,age from employee where age > 25 and age < 30;  选择年龄大于25并且小于30
- select name,age from employee where age between 25 and 30;  选择年龄在25和30区间且包含边界值的人；

## in / not in
- select name,age form employee where age in (25, 27, 30);  筛选年龄在选定的值内的人；即年龄正好是25，27，30的人
- select * from employee where in_dpt not in('dpt1', 'dpt4');  筛选‘in_dpt’不等于“dpt1", "dpt4"的人；

## like 和通配符
- like通常和通配符一起使用，通配符代表未知字符，
- SQL中的通配符是"_" 和 "%";
- "_" 代表一个为未指定字符
- "%" 代表不定个未指定字符

### 实例
- select * from employee where name like 'w%'; 查询名字以w开头的人
- select * from students where name like '_红';

## order by 排序
- order by 可以对结果进行排序，默认是升序，
- 可以指定关键词进行排序方式； 
- ‘asc’ 升序
- ‘desc’ 降序
- order by 字句一定要放在where的后面
- ` select * from app1_areatree where type='country' and date='02.18' order by totalConfirm desc;`

## 分页
- limit 3 offset 2; 查询第2页，每页显示3条
- limit 2,3 同上，简写形式
- 随着offset的值越大，查询效率会越低

## 聚合查询
- count 可以统计总数
- select count(*) boys from students;
- select count(*) boys from students where gender='M';
- select avg(score) avg,gender,class_id from students group by class_id, gender; 查询出每个班级男生女生的平均分

### 实例
- select * from pet order by name desc, age asc; 同时对多个列进行排序，名称按照升序，年龄按照降序排列。

### 实例
- select * from employee order by in_dpt desc;  按照降序排序

## SQL内置函数和计算
- count 计数， 任何数据类型，只是计数
- sum 求和，数字类型
- avg 平均值， 数字类型
- max 最大值， 数值/ 字符串/ 日期时间数据
- min 最小值， 数值/ 字符串/ 日期时间数据

### 实例
- select max(age) from employee;  找到年龄最大的人
- select max(age) as max_age from employee; 找到年龄最大的人
	- as 对max(age)进行重命名‘max_ag'

## 子查询
- 有时候先要查询的数据需要涉及多个表才能获取所需要的信息，
- 子查询只有在结果来自一个表时才有用。

### 实例
- select of_dpt, count(proj_name) as count_project from project where of_dpt in (select in_dpt from employee where name='Tom');   查询Tom所在项目组完成的项目个数。
- select students.name,classes.name from students,classes where students.class_id=classes.id order by students.score desc; 查询学生名称/ 学生所在班级，并且按照学生的成绩降序排序

## 连接查询 join
- 如果想要显示俩个表或多个表中的数据，这时就必须使用join操作
- 连接的思想就是把俩个或多个表连接成一个新的表来操作。
- 当from字句连接俩个表，因为查询需要从俩个表中提取信息；
- 如果要将一个表的记录和该表的其他记录进行比较，可以将该表联结到自身
	- select p1.name, p1.sex, p2.name, p2.sex from pet as p1, pet as p2 where p1.species=p2.species and p1.sex='f' and p2.sex='m'  查找pet表中可以进行交配的动物

### 实例
- select id,name,people_num from employee, department where employee.in_dpt=department.dpt_name order by id;  查询各员工所在部门的人数，并且结果按照id排序
- select id,name,peopel_num from employee join department on employee.id_dpt=department.dpt_name order by id; 结果和上面一样。
- select students.name,classes.name from students join classes on students.class_id=classes.id;
- select s.name,c.name,s.score from students s inner join classes c on s.class_id = c.id; 内连接

## 查询版本/ 时间
- select version(); // 获取mysql版本
- select current_date; // 获取当前日期
- select curdate(); // 获取当前日期
- select current_time; // 获取当前时间
- select 1+5; // 进行简单的计算
- select now(); // 获取当前日期和时间
- select now(); select version(); // 可以在一行同时输入多条命令；

---

# 技巧
- 查询某列最大值所在的行
	- select * from shop where price=(select max(price) from shop);
	- select * from shop order by price desc limit 1; 对所有内容按照price降序排列限制为1
- 找出每一类中价格最高的
	- select article, max(price) as price from shop group by article;

## 使用用户变量 [深入mysql用户变量](http://blog.ihuxu.com/explaination-of-the-mysql-variables-usage-and-the-use-case/#mysql-user-defined-variables)
- 通过用户变量找出价格最高和最低的物品
	- select @min_price:=min(price), @max_price:=max(price) from shop;
	- select * from shop where prce=@min_price or price=@max_price;
	- 这样就找出了价格最高和最低的物品
	- 如果新插入表格值，此时之前定义的用户变量并不会动态更新，它存储的只是创建变量当时的状态，

## 使用俩个关键字进行搜索
	- select id, color from shirt where id=1 or color='blue' ;
	- select id, color from shirt where id=1 union select id, color from shirt where color='blue';
	- 上面俩个效果是一样的，都是对id和color俩个关键字进行过滤搜索
