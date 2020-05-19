---
title: password
date: 2020-05-19 16:48:34
modify: 
tags: [Notes]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# password

## 概要

- mysql安装完成后会生成一个密码在/var/log/mysqld.log

## 使用

- `cat /var/log/mysqld.log | grep password`
- `mysql -u root -p` 使用该密码登录
- `ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass4!';`

## 参考

- [mysql 密码初始化](https://www.jianshu.com/p/a355bbf11d07)
