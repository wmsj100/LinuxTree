# SQL约束

- 通常MySQL有以下几种约束
	- PRIMARY KEY 主键
		- 用于约束表中的一行，作为这一行的唯一标识符，
		- 在一张表种通过主键就可以精确定位到某一行；
	- DEFAULT 默认值 
		- 当有default约束列时，插入数据为空，将使用默认值。
	- UNIQUE 唯一
		- 规定一张表中指定的一列值必须不能有重复值。
	- FOREIGN KEY 外键
		- 既能确保数据完整性，也能表现表之间的关系。
		- 一个表可以有多个外键，
		- 每个外键必须references(参考)另一个表的主键
		- 被外键约束的列，取值必须在参考的列中有对应的值。
		- alter table t1 add foreign key t1(fk_id) references t2(id);
			- t1(fk_id) t1 是外键名，fk_id 为当前表对应的列名
			- t2(id) 所要参考的表t2的id列
		- alter table t1 drop foreign key 'fk_id' 删除外键
		- 如果表在添加外键之前先插入了一些非法数据，然后再添加外键，之前的非法数据会被保留。
		- 给表添加外键的方法是先创建表，然后通过修改表的列属性来添加外键
	- NOT NULL 非空
		- 插入值时必须非空
		- 如果为空，会出现警告，但还是会插入成功

- auto_increment 自增

