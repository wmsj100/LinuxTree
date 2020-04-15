---
title: leveldbjni_error
date: 2020-04-15 09:23:38
modify: 
tags: [Notes]
categories: KunPen
author: wmsj100
email: wmsj100@hotmail.com
---

# leveldbjni_error

## 概要

- 是关于编译leveldbjni的编译报错

## Re: failed make: "'aclocal-1.14' is missing on your system"

- 这个是因为autoconf编译错误，没有按照要求的编译顺序开始执行
- `./autogen.sh`
- `./configure`
- `make`
- [参考文档，gnu官方文档](https://lists.gnu.org/archive/html/guile-user/2016-05/msg00022.html)

## 参考

- [华为鲲鹏社区](https://support.huaweicloud.com/prtg-hdp-kunpengbds/kunpengambarihdp_02_0009.html)
