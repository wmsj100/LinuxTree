---
title: startup_error
date: 2020-08-18 21:16:59
modify: 
tags: [Notes]
categories: Oracle
author: wmsj100
email: wmsj100@hotmail.com
---

# startup_error

## 概要

- oracle关闭后重启失败
- 原因是我设置了`alter system set processes = 10000 scope = spfile; `导致内存超，所以启动报错共享内存不足
- 无法重启oracle

## 解决

- `create pfile=’/home/oracle/db12c.ora’ from spfile;`
- 找到该文件，并且修改
- `startup  pfile=’/home/oracle/db12c.ora’ ;`
- `create spfile from pfile;`
- `shut immediate;`
- `startup;`

## 参考

- [参考](https://orahow.com/ora-04031-unable-to-allocate-bytes-of-shared-memory-during-oracle-startup/)
