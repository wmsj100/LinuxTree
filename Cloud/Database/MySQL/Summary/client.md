---
title: client
date: 2020-03-08 20:12:37
modify: 
tags: [Summary]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# client

## 概要

- 今天测试使用mysql来连接远端腾讯云的数据库时候才忽然意识到本地只需要安装mysql-client就可以了.
- 但是如果安装mysql-server时候会自动安装mysql-client,
- 现在数据库就使用远端数据库,这样更加和现实情况符合,只是想着如果直接用账户和秘密连接是否安全,
- 但现在django连接数据库也是使用账号密码的方式进行的,应该不存在那样的顾虑.

## 参考

