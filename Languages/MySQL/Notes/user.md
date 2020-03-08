--- 
title: 创建用户
date: 2019-09-13 10:17:17 Friday	
modify: 2020-03-02 08:12:31 
tag: Notes
categories: MySQL
auth: wmsj100
email: wmsj100@hotmail.com
---

# 创建用户

- create user pi@localhost identified by 'pi' 创建用户并设置密码
- create user 'wmsj100'@'localhost' 创建wmsj100
- drop user 'wmsj100'@'localhost' 删除用户
- rename user 'wmsj100'@'localhost' to 'wmsj'@'localhost'; 重命名用户
- set password for 'wmsj'@'localhost' = password('wmsj123'); 给用户wmsj设置密码“wmsj123；

## 用户授权
- `grant select,insert,update,delete on python_test.* to pi@'localhost' identified by 'pi';` 添加用户对数据库的python_test的增删改查权限
- `select * from mysql.db where user='pi'\G;` 查看用户的数据库权限
- `revoke insert on test.* from 'user1'@'localhost'; 回收user1对数据库test所有表的插入权限
- `show grants from user1;` 查看用户user1的所有权限
- `show grants for 'ubuntu'@'localhost'` 查看用户的所有权限
- `grant ALL PRIVILEGES on flask1.* to 'ubuntu'@'localhost';` 把数据库flask1的所有权限都授权给ubuntu.*

## 允许远程登陆mysql

- 查看mysql配置,是否有限制只能本地登陆.
- `sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf` 注释`#bind-address       = 127.0.0.1`
- `sudo service mysql restart`
- 配置用户允许从所有ip来访问
	- `sudo mysql`
	- `use mysq;`
	- `select user,host from user` 查看当前mysql的用户表
	- `grant all privileges on django_study4.* to 'wmsj100'@'%' identified by 'wmsj100@123'` 创建一个用户mysql,运行用户从任意ip登陆
	- `flush identified` 刷新缓存
- `mysql --host=192.168.0.2 -u wmsj100 -p -A` 输入秘密就可以了
- 添加`-A`参数连接mysql时候不会去预读列表,这种情况是因为mysql表变大了,读取速度变慢导致的,
```
mysql> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A
```

## 修改用户名

- `set password for ubuntu@localhost=password('123456')` 修改密码为123456

## 参考
- [mysql权限](https://www.cnblogs.com/Csir/p/7889953.html)
- [mysql权限范例](https://www.cnblogs.com/wangchaoyuana/p/7545419.html)
- [mysql数据库授权](https://www.cnblogs.com/NiceCui/p/8588361.html)
- [mysql远程连接](https://blog.csdn.net/sqlquan/article/details/99844820)
- [mysql reading table information for compltion](https://www.cnblogs.com/linga/p/9558201.html)
