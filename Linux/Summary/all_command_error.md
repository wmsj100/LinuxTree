---
title: all_command_error
date: 2020-03-31 18:44:14
modify: 
tags: [Summary]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# all_command_error

## 概要

- 刚刚同事的系统出问题，系统所有的命令都无法生效，ls这些基础命令也无法使用
- 我刚开始想的是文件的权限问题，发现cat等命令也无法用
- 然后我就想到了应该是PATH的值有问题了，然后查看了PATH值，发现只有一个软件的路径，之前的bin的目录都丢失了。
- 重新赋值PATH后就好了。
- 这算是我解决的第一个运维问题吧。

## 参考

