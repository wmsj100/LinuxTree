---
title: 外键
date: 2019-04-09 22:33:32	
modify: 2020-10-13 10:29:45  
tag: [key]
categories: MySQL
author: wmsj100
mail: wmsj100@hotmail.com
---

# 外键

## 概述
- 通过定义外键，关系型数据库可以保证无法插入无效的数据

## 创建
- alter table student add constraint fk_class_id foreign key (class_id) references class(id)
	- fk_class_id 外键约束名称可以任意指定
	- foreign key (class_id) 指定了class_id作为外键
	- reference class(id) 指定了这个外键将关联到class表的`id`列
- 由于外键约束会降低数据库性能，大部分互联网应用程序为了追求速度，并不设置外键约束，而是仅靠应用程序自身来保证逻辑的正确性。
- alter table student drop fk_class_id; 删除表格的外键

## 总结

- 如果一个当前表的字段被其他表当作外键引用，删除当前表之前需要先删除其他表的外键引用，直接删除当前表会导致mysql报错。
- 先删除其他表对当前表的外键引用
- 删除当前表

## 参考
- [外键](https://www.liaoxuefeng.com/wiki/001508284671805d39d23243d884b8b99f440bfae87b0f4000/00152781979845823af16bd78094353a46c8f601ae34937000)
