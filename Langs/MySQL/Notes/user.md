--- 
title: 创建用户
date: 2019-09-13 10:17:17 Friday	
tag: Notes
categories: MySQL
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

## 参考
- [mysql权限](https://www.cnblogs.com/Csir/p/7889953.html)
- [mysql权限范例](https://www.cnblogs.com/wangchaoyuana/p/7545419.html)
