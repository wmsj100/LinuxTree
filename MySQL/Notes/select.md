# select 选取数据

- select name,age from employee;
- select name,age from employee where age > 25; 
- select name,age,phone from employee where name='Mary'; 查询Mary的信息

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

## order by 排序
- order by 可以对结果进行排序，默认是升序，
- 可以指定关键词进行排序方式； 
- ‘asc’ 升序
- ‘desc’ 降序

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

## 连接查询 join
- 如果想要显示俩个表或多个表中的数据，这时就必须使用join操作
- 连接的思想就是把俩个或多个表连接成一个新的表来操作。

### 实例
- select id,name,people_num from employee, department where employee.in_dpt=department.dpt_name order by id;  查询各员工所在部门的人数，并且结果按照id排序
- select id,name,peopel_num from employee join department on employee.id_dpt=department.dpt_name order by id; 结果和上面一样。

## 查询版本/ 时间
- select version(); // 获取mysql版本
- select current_date; // 获取当前日期
- select curdate(); // 获取当前日期
- select current_time; // 获取当前时间
- select 1+5; // 进行简单的计算
- select now(); // 获取当前日期和时间
- select now(); select version(); // 可以在一行同时输入多条命令；

