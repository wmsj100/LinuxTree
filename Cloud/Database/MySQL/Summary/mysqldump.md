---
title: mysqldump
date: 2020-10-28 20:25:36
modify: 
tags: [Summary]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# mysqldump

## 概要

- 使用mysqldump来恢复数据的时候最好是一个空白的数据库，如果之前已经有数据，那么最好手动清理，否则执行导入时候会一直卡再导入界面，
- 尤其是数据量比较大的时候，
- 测试5M的sql文件，导入之前已经有接近5M的数据，导入过程中mysql一直占用接近20%的内存，但数据全部删除了，没有写入数据，保持导入界面接近10min还是没有停止，
- 手动停止，删除mysql的所有data数据，重启启动空白mysql容器，执行mysqldump导入操作，秒完成。
