# 修改和删除

## 重命名表
- alter table table_1 rename table_2;
- alter table table_1 rename to table_2;
- rename table table_1 to table_2;

- drop table table_1; 删除表；

## 添加一列
- alter table employee add height int(4) default 170;
- 可以使用after 指定插入列的位置
- 可以使用first插入到第一行
- alter table employee add weight int(4) after age;

## 删除一列
- alter table employee drop height; 删除一列

## 重命名列
- alter table employee change weight wh int(4);

## 改变列的数据类型
- alter table employee modify height varchar(12) 

## update 修改值
- update employee set age=31,salary=4000 where name='Tom';

## delete 删除
- delete from employee where name='Alex';
