# 自动增长

- 一般这个属性是添加到id或num等数值
- create table animals(id mediumint not null auto_increment, name char(30) not null, primary key(id));

## 修改auto_increment的起始值
- alter table person auto_increment=100; 修改起始值为100；
- 从上面的例子可以知道每个表只可以设置一个auto_increment;
