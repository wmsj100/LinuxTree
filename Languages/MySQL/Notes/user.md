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
- `grant ALL PRIVILEGES on flask1.* to 'ubuntu'@'localhost';` 把数据库flask1的所有权限都授权给ubuntu.

## 修改用户名

- `set password for ubuntu@localhost=password('123456')` 修改密码为123456

## 参考
- [mysql权限](https://www.cnblogs.com/Csir/p/7889953.html)
- [mysql权限范例](https://www.cnblogs.com/wangchaoyuana/p/7545419.html)
- [mysql数据库授权](https://www.cnblogs.com/NiceCui/p/8588361.html)
