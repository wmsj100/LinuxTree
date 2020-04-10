---
title: mysqldump
date: 2020-02-14 20:31:54
modify: 2020-02-26 20:10:25 
tags: [Notes]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# mysqldump

## 概要

- 导出数据命令
- 导出操作只有root有权限

## 导出数据库指定表数据

- `sudo mysqldump django1 -u root --tables blog > /tmp/blog.sql`
- 可以同时导出多张表
- `sudo mysqldump django_study4 -u root --tables app1_articlelist app1_chinaadd app1_areatree app1_chinadayaddlist app1_chinadaylist app1_dailydeadratehistory app1_dailyhealratehistory app1_dailyhistory app1_dailynewaddhistory app1_wuhandaylist> data.sql`

## 导入数据

- `sudo mysql myweb < articlelist.sql --default-character-set=utf8`

## 参考

- [mysqldump导出](https://www.cnblogs.com/linjiqin/p/11888943.html)
