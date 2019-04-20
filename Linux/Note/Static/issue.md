---
title: issue
date: Tue 20 Feb 2018 08:18:47 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## /etc/issue 设置登陆
- /etc/issue 这个文件定制linux主机的终端界面信息
    - \d 显示本端时间的日期 2018-02-20
    - \l 显示第几个终端 tty3
    - \m 显示硬件的等级 x86_64
    - \r 显示系统的版本 相当于（uname -r）
    - \t 显示本端时间的时间

```shell
\S
Kernel \r on an \m
Date: \d \t (terminal: \l)

## /etc/motd  设置用户登陆信息
