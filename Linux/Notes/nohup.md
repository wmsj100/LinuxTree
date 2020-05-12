---
title: nohup
date: 2020-05-12 07:52:40
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# nohup

## 概要

- nohup是一个POSIX命令,用于忽略SIGHUP(signal hangg up 挂断信号).SIGHUP信号是终端注销时所发送至程序的一个信号.
- nohup命令,在默认情况下会在终端输出一个名叫nohup.out的文件
- `nohup 命令名 &` 这种命令防止在注销时命令忽略SIGUP信号,但如果命令对标准I/O文件(stdin/stdout/stderr)进行输入/输出,那么该命令仍然可能被终端挂起.
- `nohup 

## 参考

- [nohup](https://zh.wikipedia.org/wiki/Nohup)
