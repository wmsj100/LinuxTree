---
title: 自增长
date: 2019-04-09 13:55:58	
modify:
tags: [Basic]
categories: MySql
---

# 自动增长

- 一般这个属性是添加到id或num等数值
- create table animals(id mediumint not null auto_increment, name char(30) not null, primary key(id));
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `jinqian` float(5,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11111112 DEFAULT CHARSET=utf8;
## 修改auto_increment的起始值
- alter table person auto_increment=100; 修改起始值为100；
- 从上面的例子可以知道每个表只可以设置一个auto_increment;
