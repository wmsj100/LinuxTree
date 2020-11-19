---
title: no_module_name_ssl
date: 2020-11-19 16:43:36
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# no_module_name_ssl

## 概要

- 这是因为当前python版本没有_ssl模块导致的，通常出现在手动编译的Python包中
- 需要重新编译并且指定`--with-ssl`
- `./configure --with-ssl`
- `make`
- `make install`

## 参考

