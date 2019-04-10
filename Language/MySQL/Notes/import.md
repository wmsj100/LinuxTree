---
title: 导入数据
date: 2019-04-10 07:58:03	
modify:
tags: [Basic]
categories: MySQL
---

# 导入数据

- 可以把一个文件里的数据保存进一张表。

## 导入数据
- load data infile 'finename' into table talbename;
- 但是按照上面进行操作时候却报错，错误码13，查询说是权限不够，然后在博客园中找了一篇文章，说是需要添加“local”就可以了。
- mysql -uroot -p < backup.sql; 通过外部sql文件来创建/恢复表
## [导入数据失败](http://www.cnblogs.com/youxin/p/5257553.html)

## 实例
- load data local infile '/home/wmsj100/Documents/test/SQL6/in.txt' into table employee; 这样就可以插入数据成功。
# source 恢复数据库

- 用备份的文件恢复数据库。

- source backou.sql 恢复数据库
- 方法二：
	- 先创建一个空的数据库test1
	- mysql test1 < backup.sql; 这样也同样可以恢复数据库的内部结构。 
