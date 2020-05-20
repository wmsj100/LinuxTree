---
title: bin_log
date: 2020-05-20 09:47:18
modify: 
tags: [Notes]
categories: MySQL
author: wmsj100
email: wmsj100@hotmail.com
---

# bin_log

## 概要

- bin_log就是binary log，二进制日志文件，这个文件记录了mysql所有的dml操作。
- 通过binlog日志我们可以做数据恢复，实现主从复制。

## 查看

- `show variables like '%log_bin%';`
```

mysql> show variables like '%log_bin%';
+---------------------------------+-----------------------------+
| Variable_name                   | Value                       |
+---------------------------------+-----------------------------+
| log_bin                         | ON                          |
| log_bin_basename                | /var/lib/mysql/binlog       |
| log_bin_index                   | /var/lib/mysql/binlog.index |
| log_bin_trust_function_creators | OFF                         |
| log_bin_use_v1_row_events       | OFF                         |
| sql_log_bin                     | ON                          |
+---------------------------------+-----------------------------+
```

## 参考

- [mysql bin-log](https://blog.csdn.net/king_kgh/article/details/74800513)
