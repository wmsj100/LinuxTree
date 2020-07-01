---
title: showLog
date: 2020-07-01 20:47:28
modify: 
tags: [Note]
categories: Shell
author: wmsj100
email: wmsj100@hotmail.com
---

# showLog

## 概要

- shell中经常会遇到要打印错误行号，报错函数，错误文件等信息

## 全局变量

- `$ $LINENO $FUNCNAME $BASH_SOURCE
- `$LINENO` 打印当前行号
- `$FUNCNAME` 打印报错函数名称
- `$BASH_SOURCE` 打印报错文件，这种可以应对通过source进来的脚本的报错定位，会直接定位到文件本身

## 参考

