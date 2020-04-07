---
title: tar (child): lbzip2: Cannot exec: No such file or directory
date: 2020-04-07 11:30:56
modify: 
tags: [Summary]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# tar (child): lbzip2: Cannot exec: No such file or directory

## 概要

- 用tar解压bz2压缩包时候报错，
- 当前系统未安装bzip2
- `yum install bzip2`

## 无网安装

- tar zxvf bzip2-1.0.6.tar.gz
- cd bzip2-1.0.6/
#为编译做准备，创建libbz2.so动态链接库(这一步很重要，安装python的时候如果没有这一步，python安装不上bz2模块)：
- make -f Makefile-libbz2_so
- make && make install

## 参考

- [tar bzip2 error](https://blog.csdn.net/u012949658/article/details/55001179)
