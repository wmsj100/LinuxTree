---
title: proc
date: 2019-05-11 22:55:51 Saturday
modify:
tag: [proc]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# proc

## 概述
- 程序： 不太精确地说，程序就是执行一系列有逻辑/有顺序结构的指令。
- 进程： 是程序在一个数据集合上的一次执行过程。
- 程序是为了完成某种任务而设计的软件，而进程是运行中的程序。
- 每个进程都有一个唯一的进程标识符，一个在1~32000的数字

## 文件介绍
- `/proc/net/socket` 查看网络套接字使用统计
- `/proc/sys/fs/file_max` 查看系统所有运行的程序可以同时打开的文件总数，其实就是文件句柄限制
- `echo 8000 > /proc/sys/fs/file_max` 修改文件的句柄数，需要root权限执行

## 进程目录
- `cmdline` 当前进程名称
- `fd` 当前进程的文件描述符

## 范例

## 参考
- []()

