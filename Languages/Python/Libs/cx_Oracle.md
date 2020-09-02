---
title: cx_Oracle
date: 2020-09-02 09:36:09
modify: 
tags: [Libs]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# cx_Oracle

## 概要

- 这个库是连接oracle的库，有linux和windows的客户端
- 该库的使用要依赖于client

## windows

- `https://download.oracle.com/otn/nt/instantclient/122010/instantclient-basiclite-windows.x64-12.2.0.1.0.zip?xd_co_f=398aa7cb-5498-42b9-9c37-acb34484372f`
- 设置环境变量
```
ORACLE_HOME = C:\instantclient_11_2
TNS_ADMIN = C:\instantclient_11_2
NLS_LANG = SIMPLIFIED CHINESE_CHINA.ZHS16GBK
```

## linux

- `sudo apt install libaio1`
- `sudo yum install libaio`
- `export LD_LIBRARY_PATH=/opt/instantclient_12_2`

## 参考

