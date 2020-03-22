---
title: localtime_error
date: 2020-03-23 07:52:33
modify: 
tags: [Summary]
categories: ArchLinux
author: wmsj100
email: wmsj100@hotmail.com
---

# localtime_error

## 概要

- 是昨天发现的当前计算机时间是错误的,当时想着是需要在设置里找那个自动同步的设置
- 但是过了一遍设置没有找到时间的设置,然后就不了了之了,刚刚忽然想到自己在安装系统时候好像没有设置localtime,
- 然后回去找系统安装步骤,发现是有这个操作的,然后设置软链接,同步硬件时间,然后就好了.
- 所以出现问题就去解决问题,不要老想着是不是应该重装系统,我这种思维还是因为windows系统带过来的惯性思维.

## 参考

